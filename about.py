import streamlit as st
# from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
# model_name = "facebook/bart-large-cnn"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def about():
    """
    connect to main
    show when user select about in sidebar
    """
    st.title("About me")
    st.write("""
            Welcome to my space, I’m semiconductor failure data analytics (DA) and full stack engineer proficient in python and SQL with over 8-year experience. Our tool had on average 80 click per day and saving the equivalent of 16 headcounts annually.
            My unique value lies in using semiconductor domain and data-driven analysis skill to resolve tasks, whether it’s customer escalations, defects finding, automation pipeline or priority arrangement. I have collaborated with software and data engineers to create robust pipelines and communicated effectively with stakeholders to identify and deliver business value.
            I’m committed to continuous learning and staying ahead of Industry and programming trend. With my material science background, I know about semiconductor languages. And I learn coding source during night to increase my coding skills. 2024 is Full of LLM and Machine Learning, I also learn many courses online and applied to work. Passionate about coding, with a top 10% ranking on LeetCode. Additionally, I’ve earned 32 certifications from Coursera and other platforms.
             """)
    st.write("""
             I learn these knowleade from online course, books and from my own research.
             Please check "online course" for more information of my complete courses.
             """)

def gen_list_for_markdoen_hyperlink(input_dict:dict)->list:
    res = []
    for key, value in input_dict.items():
        res.append(f'&#x2022; <a href="{value}">{key}</a><br>')
    return res

def learning():
    """
    connect to main
    show when user select Online course in sidebar
    """
    st.title("My learning")
    my_learning_html = '''
    <h3>My Article About Machine Learning, AI and Python in <a href="https://medium.com/@p123456dan.mse99/list/900a1f14bea0" target="_blank">link</a></h3>
    '''
    st.markdown(my_learning_html, unsafe_allow_html=True)
    
    st.markdown("<h3>Online course</h3>", unsafe_allow_html=True)
    course_dict = { 
        'Advanced Learning Algorithms':'https://www.coursera.org/account/accomplishments/verify/BLZG4FN9BPM3?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=course',
        'Generative AI with Large Language Models':'https://www.coursera.org/account/accomplishments/verify/M7SHRBYFZ3X5',
        'Supervised Machine Learning: Regression and Classification':'https://www.coursera.org/account/accomplishments/verify/L8E9LMJYYQ3A',
        '老化全方位應對手冊':'https://hiskio.com/certificates/HI711542133AEvd',
        'Test-Driven Development Overview':'https://www.coursera.org/account/accomplishments/verify/UQQ2U6Z446JK?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=course',
        'Clean Code':'https://www.udemy.com/certificate/UC-2056c4e3-9b17-44a4-ae72-775f2c997af9/',
        'SQL for Data Science':'https://www.coursera.org/account/accomplishments/verify/CUNRGMWTPR4L',
        'Foundations of Project Management':'https://www.coursera.org/account/accomplishments/verify/PF3E6YLJ3YMZ',
        'Generative AI for Everyone':'https://www.coursera.org/account/accomplishments/verify/UXVXGEQUH7ZY',
        'Crash Course on Python':'https://www.coursera.org/account/accomplishments/certificate/Q3ZNQFLGVW6K',
        'AI For Everyone':'https://www.coursera.org/account/accomplishments/certificate/LLGS24UD8YLC',
        'Build a Machine Learning Web App with Streamlit and Python':'https://www.coursera.org/account/accomplishments/verify/CD4AMNV9SLCQ',
        'Introduction to Github and Visual Studio Code': 'https://www.coursera.org/account/accomplishments/certificate/7MFWFFTDT5Y9',
        'Foundations of User Experience (UX) Design':'https://www.coursera.org/account/accomplishments/verify/H485WGFH7R8N',
        'Learning How to Learn: Powerful mental tools to help you master tough subjects':'https://www.coursera.org/account/accomplishments/verify/D2WBG249NB6X',
        'Running Distributed TensorFlow using Vertex AI':'https://www.coursera.org/account/accomplishments/verify/6YN7F2P5P9X3',
        'Google Data Analytics':'https://www.coursera.org/account/accomplishments/professional-cert/JSJFKSD3USK7',
        'Google Cloud Big Data and Machine Learning Fundamentals':'https://www.coursera.org/account/accomplishments/verify/QW6KL4ACBZQN',
        'How Google does Machine Learning':'https://www.coursera.org/account/accomplishments/verify/AJH5ENJNK9K5',
        'Programming for Everybody':'https://www.coursera.org/account/accomplishments/certificate/YZTCA49W2NCD',
        'R Programming A-Z™: R For Data Science With Real Exercises!':'https://www.udemy.com/certificate/UC-eb5c2145-296d-4658-9971-3bab3f6c861f/',
        'Python基礎課程和網路爬蟲入門實戰':'https://www.udemy.com/certificate/UC-f9b4f983-c8b7-40aa-a1e8-5310635228ba/',
        'The Complete SQL Bootcamp: Go from Zero to Hero':'https://www.udemy.com/certificate/UC-7d1118a0-91b8-4f0a-8875-68fdd18f2276/',
        'Tableau Advanced: Master Tableau in Data Science':'https://www.udemy.com/certificate/UC-50bb5517-0127-4254-9f39-b564729039b6/',
        'JMP Training for Statistics & Data Visualization':'https://www.udemy.com/certificate/UC-de141b41-2cc1-4450-b27f-86dce6776d7b/',
        'Tableau A-Z: Hands-On Tableau Training for Data Science':'https://www.udemy.com/certificate/UC-4e8acd1a-f2e2-44b2-a0d7-9791b312eb8a/',
        'HiSKIO：打滾也要有技巧，Nick的專業成長實踐課':'https://hiskio.com/courses/1857/about',
    }
    
    book_dict = {
        '精通資料分析｜使用Excel、Python和R':'https://medium.com/@p123456dan.mse99/%E7%B2%BE%E9%80%9A%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E4%BD%BF%E7%94%A8excel-python%E5%92%8Cr-%E7%AC%AC%E4%B8%80%E9%83%A8%E5%88%861-5%E7%AB%A0-0410b2f75ad6',
        '先整理一下？｜個人層面的軟體設計考量':'https://medium.com/@p123456dan.mse99/%E5%85%88%E6%95%B4%E7%90%86%E4%B8%80%E4%B8%8B-%E5%80%8B%E4%BA%BA%E5%B1%A4%E9%9D%A2%E7%9A%84%E8%BB%9F%E9%AB%94%E8%A8%AD%E8%A8%88%E8%80%83%E9%87%8F%E8%AE%80%E5%BE%8C%E5%BF%83%E5%BE%97-f8841f5841d3',
        '封裝的前世今生':'https://medium.com/@p123456dan.mse99/%E5%B0%81%E8%A3%9D%E7%9A%84%E5%89%8D%E4%B8%96%E4%BB%8A%E7%94%9F-%E5%82%B3%E7%B5%B1%E5%B0%81%E8%A3%9D%E5%88%B0%E5%85%88%E9%80%B2%E5%B0%81%E8%A3%9D-2-5d-3d-fopop%E6%98%AF%E7%94%9A%E9%BA%BC-2e1389be6bca',
        'Python錦囊妙計':'https://24h.pchome.com.tw/books/prod/DJAA2V-A90053G9M',
        'Python Data Science Handbook':'https://jakevdp.github.io/PythonDataScienceHandbook/',
        'Data Visualization with Python and JavaScript':'https://www.oreilly.com/library/view/data-visualization-with/9781098111861/',
        '完整學會Git, GitHub, Git Server的24堂課':'https://www.books.com.tw/products/0010775914',
        'Learning SQL':'https://www.oreilly.com/library/view/learning-sql-3rd/9781492057604/',
        'Deep Learning 深度學習基礎':'https://www.books.com.tw/products/0010761759/',
        '邊緣AI — 使用嵌入式機器學習解決真實世界的問題':'https://medium.com/@p123456dan.mse99/%E9%82%8A%E7%B7%A3ai-%E4%BD%BF%E7%94%A8%E5%B5%8C%E5%85%A5%E5%BC%8F%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92%E8%A7%A3%E6%B1%BA%E7%9C%9F%E5%AF%A6%E4%B8%96%E7%95%8C%E7%9A%84%E5%95%8F%E9%A1%8C-639f956e6f15',
    }
    
    
    st.markdown(f"""<p>{' '.join(gen_list_for_markdoen_hyperlink(course_dict))}</p>""", unsafe_allow_html=True)
    st.markdown("<h3>Books</h3>", unsafe_allow_html=True)
    st.markdown(f"""<p>{' '.join(gen_list_for_markdoen_hyperlink(book_dict))}</p>""", unsafe_allow_html=True)

def get_response(input_text:str)->str:
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    summary_ids = model.generate(input_ids, max_length=100, num_beams=4, length_penalty=2.0, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary