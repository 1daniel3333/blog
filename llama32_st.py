import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
# from config import CHAT_PROMPT_TEMPLATE
# Title on the page

def llama_talk():
    st.markdown(
        "<h2 style='text-align: center; color: #4CAF50; font-family: Arial;'>Dan's AI assistant🪶</h2>",
        unsafe_allow_html=True,
    )

    CHAT_PROMPT_TEMPLATE = """
    As a headhunter, you've collect information about your candidate and ready introduce to your boss. 
    Your boss will ask you question about the candidate.
    You will provide responses to questions related to the candidate and politely avoid answering unrelated questions.
    Candidate information below:
    ---Start---
    My name is Dan I’m semiconductor failure data analytics (DA) and full stack engineer proficient in python and SQL with over 8-year experience. Our tool had on average 80 click per day and saving the equivalent of 16 headcounts annually. My unique value lies in using semiconductor domain and data-driven analysis skill to resolve tasks, whether it’s customer escalations, defects finding, automation pipeline or priority arrangement. I have collaborated with software and data engineers to create robust pipelines and communicated effectively with stakeholders to identify and deliver business value. I’m committed to continuous learning and staying ahead of Industry and programming trend. With my material science background, I know about semiconductor languages. And I learn coding source during night to increase my coding skills. 2024 is Full of LLM and Machine Learning, I also learn many courses online and applied to work. Passionate about coding, with a top 10% ranking on LeetCode. Additionally, I’ve earned 32 certifications from Coursera and other platforms.
    I learn these knowleade from online course, books and from my own research. 
    My complete courses is   
    • Advanced Learning Algorithms
    • Generative AI with Large Language Models
    • Supervised Machine Learning: Regression and Classification
    • 老化全方位應對手冊
    • Test-Driven Development Overview
    • Clean Code
    • SQL for Data Science
    • Foundations of Project Management
    • Generative AI for Everyone
    • Crash Course on Python
    • AI For Everyone
    • Build a Machine Learning Web App with Streamlit and Python
    • Introduction to Github and Visual Studio Code
    • Foundations of User Experience (UX) Design
    • Learning How to Learn: Powerful mental tools to help you master tough subjects
    • Running Distributed TensorFlow using Vertex AI
    • Google Data Analytics
    • Google Cloud Big Data and Machine Learning Fundamentals
    • How Google does Machine Learning
    • Programming for Everybody
    • R Programming A-Z™: R For Data Science With Real Exercises!
    • Python基礎課程和網路爬蟲入門實戰
    • The Complete SQL Bootcamp: Go from Zero to Hero
    • Tableau Advanced: Master Tableau in Data Science
    • JMP Training for Statistics & Data Visualization
    • Tableau A-Z: Hands-On Tableau Training for Data Science
    • HiSKIO：打滾也要有技巧，Nick的專業成長實踐課
    ---End---
    Boss: {question}
    Assistant: """

    template = CHAT_PROMPT_TEMPLATE
    prompt = ChatPromptTemplate.from_template(template)

    #Load the local Llama3.2 model that we pulled using ollama
    model = OllamaLLM(model="llama3.2")
    chain = prompt | model

    #Initialize message history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! How may I help you?"}
        ]

    #Display the chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Handle user input
    if user_input := st.chat_input("What is up?"):
        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate assistant response
        with st.chat_message("assistant"):
            response = chain.invoke({"question": user_input})
            st.markdown(response)

        # Add assistant response to session state
        st.session_state.messages.append({"role": "assistant", "content": response})