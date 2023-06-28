import streamlit as st
import about

## I'm using streamlit to create my bolg, I want web browser title to set "Dan's record blog" and page title as "Welcome to Dan's space"

st.set_page_config(page_title="Dan's record blog", page_icon=":smile:", layout="wide")
st.title('Welcome to Dan\'s space')
#Good, now I want to enable a side bar to control the content of my blog

st.sidebar.title('Navigation')
#Good, now side bar should contain radio selector with some category ['Read books','Online course',]
selector = st.sidebar.radio('my category',['About me','Read books','Online course',])
if selector == 'Read books':
    st.write('You selected Read books')
elif selector == 'Online course':
    st.write('You selected Online course')
elif selector == 'About me':
    about.about()


