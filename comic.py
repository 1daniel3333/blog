from urllib import request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import os
import streamlit as st
   
def get_week_comic(comic_dict={}):
    """
    call this function to return recent week comic dict with url as value
    """
    def crawler_comic(comic_dict={}, conic_name=''):
       """
       Args:
           comic_dict (dict, optional): _description_. Defaults to {}.
           conic_name (str, optional): _description_. Defaults to ''.
       return:
              json from google result
       """
       def comic_encode(conic_name=''):
              #translate chinese to google search acceptable form
              # conic_name = '全知读者视角'
              return str(conic_name.encode('utf-8')).replace('\\x','%').split("'")[1].upper() 
       #search in google for recent 1 week and get url
       # url="https://www.google.com.tw/search?q=%E5%85%A8%E7%9F%A5%E8%AF%BB%E8%80%85%E8%A7%86%E8%A7%92+site%3Ahttps%3A%2F%2Fwww.colamanhua.com%2Fmanga-vw74000%2F&biw=1310&bih=961&tbs=qdr%3Aw&ei=9NmmZKXMHpj7-Qa-nqyoCQ&ved=0ahUKEwilluyZr_r_AhWYfd4KHT4PC5UQ4dUDCA8&oq=%E5%85%A8%E7%9F%A5%E8%AF%BB%E8%80%85%E8%A7%86%E8%A7%92+site%3Ahttps%3A%2F%2Fwww.colamanhua.com%2Fmanga-vw74000%2F&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQDEoECEEYAVDaF1jaF2DxImgCcAB4AIABJ4gBJ5IBATGYAQCgAQKgAQHAAQE&sclient=gws-wiz-serp"
       url=f"https://www.google.com.tw/search?q={comic_encode(conic_name)}+site%3Ahttps%3A%2F%2Fwww.COLAmanhua.com%2Fmanga-{comic_dict[conic_name]}%2F&tbs=qdr%3Aw"
       request_site = Request(url, headers = {'User-Agent': 'Mozilla/5.0',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
              'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
              'Accept-Encoding': 'none',
              'Accept-Language': 'en-US,en;q=0.8',
              'Connection': 'keep-alive'})
       webpage = urlopen(request_site).read()
       print('Return data below:')
       print(webpage[:500])
       return webpage
   
    def get_url(raw_json='', conic_name=''):
       """_summary_

       Args:
           raw_json (str, optional): _description_. Defaults to ''.
           conic_name (str, optional): _description_. Defaults to ''.
           
       return:
              saver: list of data
       """
       saver=[]
       soup = BeautifulSoup(raw_json, 'html.parser')
       a_tags = soup.find_all('a')
       for tag in a_tags:
       # print(tag.get('href'))
              if conic_name in tag.text:
                     test = tag.get('href')
                     test=test.split('=')[1].split('&')[0]
                     print(test)
                     if '.html' in test:
                            #sometimes there will be main page be included, exclude this
                            saver.append(test)
       return saver
    if len(comic_dict)==0:
        #assign default
        comic_dict = {
            '全知读者视角':'vw74000',
            '全职法师':'yo40340',
            '重生最强玩家':'vo74545',
            '我独自满级新手':'ox32229',
            '玄幻，我能无限顿悟':'ml32386',
            '死灵法师：亡灵支配者':'ky84590',
            '我可以无限顿悟':'rq68930',
            '炼体十万层：我养的狗都是大帝':"ke39760",
            '99强化木棍':"kh997348",
        }

    week_comic = {}
    for comic_name in comic_dict:
        raw_json = crawler_comic(comic_dict,comic_name)
        tmp_url_lists = get_url(raw_json, comic_name)
        if len(tmp_url_lists)>0:
            for tmp_url_list in tmp_url_lists:
                week_comic[tmp_url_list]=comic_name
    return week_comic

def save_url(comic_dict:{}, save_file_name=''):
    """
    Input parameter:
     dict from crawler
    Function:
        update csv to latest
    """
    # save_file_name = "comic.csv"
    def new_comic_df(comic_dict={}):
        """_summary_
        
        Args:
            comic_dict (dict, optional): _description_. Defaults to {}.

        Returns:
            _type_: dataframe
        """
        comic_df = pd.DataFrame(columns=['title','number','url','check','add_date'])
        today = date.today()
        for url in comic_dict:
            comic_df.loc[len(comic_df)]=[comic_dict[url],f"{url.split('/')[-1].split('.')[0]}",url,'',today]
        return comic_df

    if not os.path.isfile(save_file_name):
        readed_csv = new_comic_df(comic_dict)
    else:
        #input there's crawler dict

        #read previous saved csv
        readed_csv=pd.read_csv(save_file_name)

        # extract old url
        old = list(readed_csv['url'])

        #new url to list
        new = list(comic_dict.keys())

        #get new find url as list
        new_find = [x for x in new if x not in old]

        #append new list to dataframe
        for url in new_find:
            today = date.today()
            readed_csv.loc[len(readed_csv)]=[comic_dict[url],f"{url.split('/')[-1].split('.')[0]}",url,'',today]
        
    #save to csv
    readed_csv.to_csv(save_file_name, index=False,encoding='utf-8-sig')
    
def update_check(url_list=[]):
    """_summary_

    Args:
        url_list (list, optional): _description_. Defaults to [].

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_ return "Save complete"
    """
    saving_name = 'comic.csv'
    comic_df = pd.read_csv(saving_name)
    for url in url_list:
        try:
            location = comic_df[comic_df['url']==url].index[0]
            comic_df.loc[location,['check']] = 'YES'
        except:
            raise ValueError('Cannot find url')
    comic_df.to_csv(saving_name, index=False)
    return 'Save complete'