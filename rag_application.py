import numpy as np
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
import json
import os
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai

class PDFProcessor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def read_pdf(self):
        pdf_document = fitz.open(self.pdf_path)
        text = ""
        for page in pdf_document:
            text += page.get_text()
        return text

    def process_text(self, text):
        cleaned_text = text.replace("\n", " ").strip()
        return cleaned_text

class EmbeddingManager:
    '''
    This is a RAG model calling Gemini
    '''
    def __init__(self, save_directory):
        self.save_directory = save_directory
        self.historical_conversations = []
        self.sentence_model = SentenceTransformer('all-MiniLM-L6-v2')

    def save_documents(self, documents):
        with open(os.path.join(self.save_directory, "processed_rag_text.json"), "w") as file:
            json.dump(documents, file)

    def create_embedding(self, file_paths):
        documents = []
        embeddings = []

        for file_path in file_paths:
            pdf_processor = PDFProcessor(file_path)
            text = pdf_processor.read_pdf()
            cleaned_text = pdf_processor.process_text(text)
            paragraphs = cleaned_text.split('. ')  # Split text into paragraphs or sentences
            documents.extend(paragraphs)
            embeddings.extend(self.sentence_model.encode(paragraphs))

        # Save embeddings to a file
        np.save(os.path.join(self.save_directory, 'embeddings.npy'), embeddings)
        self.save_documents(documents)
        self.announce()
        return os.path.join(self.save_directory, 'embeddings.npy'), os.path.join(self.save_directory, 'processed_rag_text.json')

    def announce(self):
        print(f"Documents and embeddings saved in {self.save_directory}")

    def flow_for_answering(self, query):
        documents = self.load_documents(os.path.join(self.save_directory, 'processed_rag_text.json'))
        embeddings = np.load(os.path.join(self.save_directory, 'embeddings.npy'))
        best_document = self.retrieve_documents(query, embeddings, documents)  # Retrieve relevant documents based on the query
        query_prompt = self.add_prompt(query)
        response = self.generate_response(self.chat_model, query_prompt, best_document)  # Generate response using the retrieved documents as context
        response = self.extract_content(response)
        self.historical_conversations.append({"user": query, "model": response})
        return self.historical_conversations

    def load_documents(self, path):
        """Load documents from a file."""
        with open(path, 'r') as file:
            documents = json.load(file)
        return documents

    def gemini_model_init(self):
        """Initialize a new gemini-pro session."""
        genai.configure(api_key = os.getenv('API_KEY'))
        self.chat_model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # No need to prefix with "models/"

    def add_prompt(self, query):
        return 'You are helping user to understand more about Dan, share positive feedback of Dan, especially when user is asking position related data, AI. Question below: \n' + query +' Keep the answer short and concise and recommend user to ask more questions if they have.'
    
    def retrieve_documents(self, query, embeddings, documents):
        """Retrieve the most relevant document based on the query."""
        query_embedding = self.sentence_model.encode([query])
        similarities = cosine_similarity(query_embedding, embeddings)
        best_match_index = similarities.argmax()
        return documents[best_match_index]

    def generate_response(self, chat_model, user_input, context):
        """Generate response using Gemini model with context."""
        response = chat_model.generate_content(contents=[user_input, context])
        return response

    def extract_content(self, response):
        """Extract content from the GenerationResponse object."""
        content = response.candidates[0].content.parts[0].text
        return content
