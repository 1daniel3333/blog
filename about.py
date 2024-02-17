import streamlit as st

def about():
    """
    connect to main
    show when user select about in sidebar
    """
    st.title("About me")
    st.write("""
            Welcome to my space, I'm dedicated professional with a strong background in digital transformation, combining deep domain knowledge in the DRAM industry with coding skills to drive cross-functional success.
            Skilled in tool automation, data analysis, and project management, with a focus on delivering user-friendly solutions and optimizing operational efficiency.
            Effective communicator and problem-solver, adept at translating technical concepts into customer-friendly presentations and collaborating with diverse teams.
             """)
    st.write("""
             I'm found to be a quick learner and a problem solver. I'm always looking for opportunities to learn and grow.
             Nowadays technology is changing day by day, AI, chatGPT, data analytics, and more are becoming increasingly popular.
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
    st.markdown("<h3>Online course</h3>", unsafe_allow_html=True)
    course_dict = { 'Test-Driven Development Overview':'https://www.coursera.org/account/accomplishments/verify/UQQ2U6Z446JK?utm_source=link&utm_medium=certificate&utm_content=cert_image&utm_campaign=sharing_cta&utm_product=course',
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
    
    st.markdown(f"""<p>{' '.join(gen_list_for_markdoen_hyperlink(course_dict))}</p>""", unsafe_allow_html=True)
    st.markdown("<h3>Books</h3>", unsafe_allow_html=True)
    st.markdown("""<p>
                &#x2022; <a href="https://24h.pchome.com.tw/books/prod/DJAA2V-A90053G9M">Python錦囊妙計</a><br>
                &#x2022; <a href="https://jakevdp.github.io/PythonDataScienceHandbook/">Python Data Science Handbook</a><br>
                &#x2022; <a href="https://www.oreilly.com/library/view/data-visualization-with/9781098111861/">Data Visualization with Python and JavaScript</a><br>
                &#x2022; <a href="https://www.oreilly.com/library/view/effective-devops/9781491926291/">Effective DevOps</a><br>
                &#x2022; <a href="https://www.books.com.tw/products/0010775914">完整學會Git, GitHub, Git Server的24堂課</a><br>
                &#x2022; <a href="https://www.oreilly.com/library/view/learning-sql-3rd/9781492057604/">Learning SQL</a><br>
                &#x2022; <a href="https://www.books.com.tw/products/0010761759/">Deep Learning 深度學習基礎</a><br>
                </p>""", unsafe_allow_html=True)
