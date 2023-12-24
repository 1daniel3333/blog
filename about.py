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
    
def learning():
    """
    connect to main
    show when user select Online course in sidebar
    """
    st.title("My learning")
    st.markdown("<h3>Online course</h3>", unsafe_allow_html=True)
    st.markdown("""<p>
                &#x2022; <a href="https://www.coursera.org/learn/project-management-foundations/">Foundations of Project Management</a><br>
                &#x2022; <a href="https://www.coursera.org/learn/generative-ai-for-everyone/">Generative AI for Everyone</a><br>
                &#x2022; <a href="https://www.coursera.org/learn/ai-for-everyone">Coursera- AI for Everyone</a><br>
                &#x2022; <a href="https://www.coursera.org/professional-certificates/google-data-analytics">Coursera- Google Data Analysis</a><br>
                &#x2022; <a href="https://www.coursera.org/learn/python">Coursera - Programming for Everybody (Getting Started with Python)</a><br>
                &#x2022; <a href="https://www.coursera.org/learn/learning-how-to-learn">Coursera - Learning How to Learn: Powerful mental tools to help you master tough subjects</a><br>
                &#x2022; <a href="https://www.coursera.org/projects/machine-learning-streamlit-python">Coursera - Build a Machine Learning Web App with Streamlit and Python</a><br>
                &#x2022; <a href="https://www.udemy.com/course/the-complete-sql-bootcamp/">Udemy- SQL Bootcamp 2022: Go from Zero to Hero</a><br>
                &#x2022; <a href="https://www.udemy.com/course/tableau10/">Udemy- Tableau 2020 A-Z:Hands-on Tableau Training for data science</a><br>
                &#x2022; <a href="https://www.udemy.com/course/tableau10-advanced/">Udemy- Tableau 20 Advanced Training Master Tableau in Data Science</a><br>
                &#x2022; <a href="https://www.udemy.com/course/complete-uipath-rpa-developer-course/">Udemy- Complete Uiath RPA Developer Course: Build 7 Robots</a><br>
                &#x2022; <a href="https://www.udemy.com/course/jmp-2020-hands-on-jmp-training-for-statistics/">Udemy- JMP Training for Statistics % Data Visualization</a><br>
                &#x2022; <a href="https://www.udemy.com/course/codegym-python/">Udemy- Python 基礎課程和網路爬蟲入門實戰</a><br>
                &#x2022; <a href="https://www.udemy.com/course/best-unix-linux-training-for-software-qa-testers/">Udemy- Unix, Linux training for beginners</a><br>
                &#x2022; <a href="https://www.udemy.com/course/project-management-improve-project-manager-skills/">Udemy- Project Management: The Closing Phase</a><br>
                &#x2022; <a href="https://www.udemy.com/course/r-programming/">Udemy- R Programming A-Z™: R For Data Science With Real exercises</a><br>
                &#x2022; <a href="https://hiskio.com/courses/1857/about">HiSKIO：打滾也要有技巧，Nick的專業成長實踐課</a><br>
                </p>""", unsafe_allow_html=True)
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
