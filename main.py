import streamlit as st
import about
import blogs
import medium
import suscribe
import pandas as pd
from streamlit.components.v1 import html

def read_books(key):
    st.write(blogs.book_dict[key])

def tag_create():
    """
    read blod context and find # to generate a tag dic.
    """
    tags_key = {}
    for key,values in blogs.book_dict.items():
        tags = values.split('#')
        if len(tags) > 1:
            ## remove \n and space
            tags = [x.replace("\n", "").replace(" ", "") for x in tags[1:]]
            for tag in tags:
                if tag in tags_key:
                    tags_key[tag].append(key)
                else:
                    tags_key[tag] = [key]
    return tags_key

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

def decide_action_on_selection(selector:str):
    if selector == 'Read books':
        tags_key=tag_create()
        #add key to display how many post have the same tag
        post_dict={}
        for key,values in tags_key.items():
            post_dict[f'{key}: {len(values)} post(s)']=key
        check_tags=st.sidebar.selectbox('Tags',['All']+list(post_dict.keys()))
        #base on selection, use two dic conversion to filter articles
        if check_tags == 'All':
            check_blog=st.sidebar.selectbox('Blogs',blogs.book_dict.keys())
        else:
            check_blog=st.sidebar.selectbox('Blogs',list(tags_key[post_dict[check_tags]]))
        st.title(check_blog)
        read_books(check_blog)
    elif selector == 'my articles':
        st.title('Some recent Article:')
        with st.spinner('Retrieving data'):
            blog_dic = medium.get_medium_dict()
        for key,value in blog_dic.items():
            st.markdown(f'<h3><a href="{value["url"]}">{key}</a></h3>', unsafe_allow_html=True)
            st.markdown(value["content"])
        
    elif selector == 'Online course':
        about.learning()
    elif selector == 'About me':
        about.about()
    elif selector == 'house trend':
        body = """
                <div class='tableauPlaceholder' id='viz1691080442321' style='width: 800px; height: 1000px;'> 
                    <noscript>
                        <a href='#'>
                        <img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ho&#47;house_trend&#47;overall_trend&#47;1_rss.png' style='border: none' />
                        </a>
                    </noscript>
                    <object class='tableauViz'  width='800' height='1000' style='display:none;'>
                        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
                        <param name='embed_code_version' value='3' /> 
                        <param name='site_root' value='' />
                        <param name='name' value='house_trend&#47;overall_trend' />
                        <param name='tabs' value='no' />
                        <param name='toolbar' value='yes' />
                        <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ho&#47;house_trend&#47;overall_trend&#47;1.png' /> 
                        <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' />
                        <param name='display_spinner' value='yes' />
                        <param name='display_overlay' value='yes' />
                        <param name='display_count' value='yes' />
                        <param name='language' value='zh-TW' />
                    </object>
                </div>                
                <script type='text/javascript'>                    
                    var divElement = document.getElementById('viz1691080442321');                    
                    var vizElement = divElement.getElementsByTagName('object')[0];                    
                    vizElement.style.width='100%';
                    vizElement.style.height='100%';                   
                    var scriptElement = document.createElement('script');                    
                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                   
                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                
                </script>"""
        html(body)
        st.markdown('''<p><a href="https://public.tableau.com/views/house_trend/overall_trend?:language=zh-TW&:display_count=n&:origin=viz_share_link">
                    House Trending Tableau form</a></p>''', unsafe_allow_html=True)
        st.info('python plot TBD.')
    elif selector == 'subscribe':
        st.title('大人學列表')
        dict = suscribe.get_big_man_rss()
        for key, value in dict.items():
            body = f"""
            <p><a href="{value}"</a>{key}</p>
            """
            st.markdown(body, unsafe_allow_html=True)
        st.title('綠角列表')
        dict = suscribe.get_green_data()
        for key, value in dict.items():
            body = f"""
            <p><a href="{value}"</a>{key}</p>
            """
            st.markdown(body, unsafe_allow_html=True)

def show_sidebar_get_selection(topic:list)->str:
    return st.sidebar.radio('my category',topic,key="para", on_change=update_params, )

def main():
    st.set_page_config(page_title="Dan's record blog", page_icon=":smile:", layout="wide")
    st.sidebar.title('Navigation')
    
    exist_topic = ['About me','Read books','my articles','Online course','house trend','subscribe']
    selector = show_sidebar_get_selection(exist_topic)
    
    if is_empty_option():
        set_option_to_default(exist_topic)
    
    decide_action_on_selection(selector)
    
if __name__ == '__main__':
    main()

