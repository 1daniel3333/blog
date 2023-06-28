import streamlit as st
import about
import blogs

## I'm using streamlit to create my bolg, I want web browser title to set "Dan's record blog" and page title as "Welcome to Dan's space"

st.set_page_config(page_title="Dan's record blog", page_icon=":smile:", layout="wide")
#Good, now I want to enable a side bar to control the content of my blog
st.sidebar.title('Navigation')
#Good, now side bar should contain radio selector with some category ['Read books','Online course',]

def read_books(key):
    st.write(blogs.book_dict[key])

selector = st.sidebar.radio('my category',['About me','Read books','Online course',])
if selector == 'Read books':
    check_blog=st.sidebar.selectbox('Blogs',blogs.book_dict.keys())
    st.title(check_blog)
    read_books(check_blog)
elif selector == 'Online course':
    about.learning()
elif selector == 'About me':
    about.about()


