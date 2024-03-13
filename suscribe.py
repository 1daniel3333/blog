from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

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