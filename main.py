import streamlit as st
import about
import blogs
import pandas as pd
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
                

selector = st.sidebar.radio('my category',['About me','Read books','Online course','house trend','comic'])
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
    st.write('New functions TBD.')
elif selector == 'comic':
    st.write('New functions TBD.')
    # ref link https://www.colamanhua.com/manga-vw74000/
    # df = pd.read_csv('save.csv')
    # st.dataframe(df)
    # st.write('change df to others')
    # df.loc[len(df)] = ['new_name', 5]
    # df.to_csv('save.csv',index=False)
    # st.download_button('Download csv',df.to_csv(),'save.csv','text/csv')


