import streamlit as st
import about
import medium
import suscribe
import pandas as pd
import house
import topic

def convert_df(df):
   return df.to_csv(index=False).encode('utf-8-sig')

def update_params():
    st.query_params['option']=st.session_state.para

def is_empty_option()->bool:
    if 'option' not in st.query_params.keys():
        return True
    return False

def set_option_to_default(option_list:list):
    st.query_params['option'] = option_list[0]

def get_action_my_atricles():
    st.title('Some recent Article:')
    with st.spinner('Retrieving data'):
        blog_dic = medium.get_medium_dict()
    for key,value in blog_dic.items():
        st.markdown(f'<h3><a href="{value["url"]}">{key}</a></h3>', unsafe_allow_html=True)
        st.markdown(value["content"])

def get_action_online_course():
    about.learning()

def get_action_about_me():
    about.about()
    import llama32_st as llm
    llm.llama_talk()

def get_action_house_trend():
    house.house_main()
    
def get_action_weather():
    topic.weather_main()

def get_action_subscribe():
    content_dict = {
        '大人學列表': suscribe.get_big_man_rss(),
        '綠角列表': suscribe.get_green_data(),
        '今日漫畫': suscribe.get_comic(),
        }
    with st.spinner('Retrieving data'):
        for title, data in content_dict.items():
            st.title(title)
            for key, value in data.items():
                body = f'<p><a href="{value}">{key}</a></p>'
                st.markdown(body, unsafe_allow_html=True)
        
def decide_action_on_selection(selector:str):
    if selector == 'My articles':
        get_action_my_atricles()
    elif selector == 'Online course':
        get_action_online_course()
    elif selector == 'About me':
        get_action_about_me()
    elif selector == 'house trend':
        get_action_house_trend()
    elif selector == 'Subscribe':
        get_action_subscribe()
    elif selector == 'Checking List':
        topic.get_list_to_check()

def show_sidebar_get_selection(topic:list)->str:
    return st.sidebar.radio('my category',topic,key="para", on_change=update_params, )

def main():
    st.set_page_config(page_title="Dan's record blog", page_icon=":smile:", layout="wide")
    st.sidebar.title('Navigation')
    exist_topic = ['About me','My articles','Online course','house trend','Checking List','Subscribe']
    selector = show_sidebar_get_selection(exist_topic)
    if is_empty_option():
        set_option_to_default(exist_topic)
    decide_action_on_selection(selector)
    
if __name__ == '__main__':
    main()