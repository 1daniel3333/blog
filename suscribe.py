from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import datetime

def big_man_cutter(data='', cutter='')->str:
    """
    A part xml get from bs4 and cutter for certain string to cut 
    """
    if (len(data)==0) or (len(cutter)==0):
        raise ValueError('No Valid data input')
    data = str(data).split(f'<{cutter}>')[1]
    data = str(data).split(f'</{cutter}>')[0]
    return data

def get_big_man_rss()->dict:
    """
    You will get a dict with key is title and value is url
    """
    url = 'https://feeds.feedburner.com/darencademy/GwRT'
    raw_html = get_web_html_by_bs4(url)
    title_raw = raw_html.select('title')[2:] #first two is header not article mark
    link_raw = raw_html.select('guid')
    if len(title_raw)!=len(link_raw):
            raise ValueError('Title and link len mismatch.')
    title = [big_man_cutter(x, 'title') for x in title_raw]
    link = [big_man_cutter(x, 'guid') for x in link_raw]
    book_dic = dict(zip(title, link))
    return book_dic

def green_cutter_list(datas:list)->dict:
    dic = {}
    for data in datas:
        dic[str(data).split('a href="')[1].split('">')[1].split('</a>')[0]]=str(data).split('a href="')[1].split('">')[0]
    return dic

def get_green_data()->dict:
    #get green first page url
    url = 'https://greenhornfinancefootnote.blogspot.com/'
    raw_html = get_web_html_by_bs4(url)
    raw = raw_html.find_all('h3', class_='post-title entry-title')
    return green_cutter_list(raw)

def get_web_html_by_bs4(url:str):
    request_site = Request(url, headers = {'User-Agent': 'Mozilla/5.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'})
    webpage = urlopen(request_site).read()
    soup = BeautifulSoup(webpage)
    return soup

def get_current_day():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today = datetime.datetime.now().weekday()
    return days_of_week[today]

def get_comic()->dict:
    comic_dict = {
        "Monday":{'第一序列':'https://www.colamanga.com/manga-pp95549/','全知读者视角':'https://www.colamanga.com/manga-gs015814/'}, 
        "Tuesday":{'我独自满级新手':'https://www.colamanga.com/manga-pl703354/'}, 
        "Wednesday":{'全球冰封：我打造了末日安全屋':'https://www.colamanga.com/manga-hy703661/'}, 
        "Thursday":{'66666年后复活的黑魔法师':'https://www.colamanga.com/manga-yg780527/'}, 
        "Friday":{'看脸时代':'https://www.colamanga.com/manga-nn727564/'}, 
        "Saturday":{'这个勇者是金钱至上主义者':'https://www.colamanga.com/manga-rp47086/','觉醒战士':'https://www.colamanga.com/manga-gg528682/'}, 
        "Sunday":{'炼体十万层：我养的狗都是大帝':'https://www.colamanga.com/manga-qq128585/','被塔诅咒的猎人':'https://www.colamanga.com/manga-dg260221/'},
    }
    current = get_current_day()
    return comic_dict[current]
    