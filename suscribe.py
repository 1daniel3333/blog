from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def get_big_man_rss():
    """
    You will get a dict with key is title and value is url
    """
    def cutter(data='', cutter=''):
        """
        A part xml get from bs4 and cutter for certain string to cut 
        """
        if (len(data)==0) or (len(cutter)==0):
            raise ValueError('No Valid data input')
        data = str(data).split(f'<{cutter}>')[1]
        data = str(data).split(f'</{cutter}>')[0]
        return data
    # check 大人學 RSS
    url = 'https://feeds.feedburner.com/darencademy/GwRT'

    request_site = Request(url, headers = {'User-Agent': 'Mozilla/5.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'})
    webpage = urlopen(request_site).read()
    # decode get xml
    soup = BeautifulSoup(webpage )
    
    title_raw = soup.select('title')[2:] #first two is header not article mark
    link_raw = soup.select('guid')
    if len(title_raw)!=len(link_raw):
            raise ValueError('Title and link len mismatch.')
    title = [cutter(x, 'title') for x in title_raw]
    link = [cutter(x, 'guid') for x in link_raw]
    book_dic = dict(zip(title, link))
    return book_dic

def get_green_data():
    def cutter_list(datas:list):
        dic = {}
        for data in datas:
                dic[str(data).split('a href="')[1].split('">')[1].split('</a>')[0]]=str(data).split('a href="')[1].split('">')[0]
        return dic
    #get green first page url
    url = 'https://greenhornfinancefootnote.blogspot.com/'

    request_site = Request(url, headers = {'User-Agent': 'Mozilla/5.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'})
    webpage = urlopen(request_site).read()
    # decode get xml
    soup = BeautifulSoup(webpage )
    #get new page title
    raw = soup.find_all('h3', class_='post-title entry-title')
    # reutnr a dict
    return cutter_list(raw)