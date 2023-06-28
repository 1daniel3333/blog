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
    st.markdown("<h3>Online course</h3>", allow_html=True)
    st.markdown("<p>Coursera- AI for Everyone</p>", allow_html=True)