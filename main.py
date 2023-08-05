import streamlit as st
import about
import blogs
import pandas as pd
import comic
from streamlit.components.v1 import html
# from save_house.house import get_file

## first attempt is in https://1daniel3333.github.io
## I'm using streamlit to create my bolg, I want web browser title to set "Dan's record blog" and page title as "Welcome to Dan's space"
st.set_page_config(page_title="Dan's record blog", page_icon=":smile:", layout="wide")
#Good, now I want to enable a side bar to control the content of my blog
st.sidebar.title('Navigation')
#Good, now side bar should contain radio selector with some category ['Read books','Online course',]

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
    st.experimental_set_query_params(option=st.session_state.para)
 
def main():
    selector = st.sidebar.radio('my category',['About me','Read books','Online course','house trend','comic','subscribe'],key="para", on_change=update_params, )
    
    query_params = st.experimental_get_query_params()
    if 'option' not in query_params:
        st.experimental_set_query_params(option=st.session_state.para)
    else:
        selector=query_params['option'][0]
        
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
    elif selector == 'comic':
        if 'comic_dict' not in st.session_state:
            st.session_state.comic_dict = comic.get_week_comic()
            comic.save_url(st.session_state.comic_dict,"comic.csv")
        
        # Read file
        comic_df_raw = pd.read_csv("comic.csv")
        #only show na data means un-check yet
        comic_df = comic_df_raw[comic_df_raw['check'].isna()].reset_index(drop=True)
        
        select_dict = {}
        if len(comic_df)>0:
            for i in range(len(comic_df)):
                select_dict[(f"{comic_df.iloc[i]['title']}:{comic_df.iloc[i]['number']}")]=comic_df.iloc[i]['url']
                body = f"""
                <p><a href="{comic_df.iloc[i]['url']}">{comic_df.iloc[i]['title']}:{comic_df.iloc[i]['number']}</a></p>
                """
                st.markdown(body, unsafe_allow_html=True)
        else:
            st.write('No unread latest comic.')
            
        select_lists= st.sidebar.multiselect('Mark check:', list(select_dict.keys()) )
        update_check = st.sidebar.button('Submit')
        
        if update_check==True:
            status = comic.update_check([select_dict[x] for x in select_lists])
            st.write(status)
            
        csv = convert_df(comic_df_raw)

        st.sidebar.download_button(
        "Download current status",
        csv,
        "comic.csv",
        "text/csv",
        key='download-csv'
        )
    elif selector == 'subscribe':
        st.title('大人學列表')
        dict = comic.get_big_man_rss()
        for key, value in dict.items():
            body = f"""
            <p><a href="{value}"</a>{key}</p>
            """
            st.markdown(body, unsafe_allow_html=True)
        st.title('綠角列表')
        dict = comic.get_green_data()
        for key, value in dict.items():
            body = f"""
            <p><a href="{value}"</a>{key}</p>
            """
            st.markdown(body, unsafe_allow_html=True)
        

if __name__ == '__main__':
    main()

