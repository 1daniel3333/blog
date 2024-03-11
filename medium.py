from selenium import webdriver
from bs4 import BeautifulSoup

def get_a_tag_from_url(url:str="https://medium.com/@p123456dan.mse99"):
    driver = webdriver.Firefox()  # or webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    a_tags = soup.find_all('a')
    driver.quit()
    return a_tags 

def get_raw_target_text(raw_bs4_txt)->list:
    saver = []
    for url in raw_bs4_txt:
        if url.find('p') and not url.find('span'):
            saver.append(url)
    return saver

def gen_dict(raw:list)->dict:
    blog_dic = {}
    for url in raw[1:]: #start from 1 because 0 is un-need
        partial_url = url['href'].split('?')[0].split('/')[-1] #extract after name, contains title and hash
        title = partial_url[:-13]
        if not title or (title=='en') or '@' in title:
            #force to stop if title null, had @ or is en
            break
        blog_dic[title]={'url':f'https://medium.com/@p123456dan.mse99/{partial_url}', 'content':url.find('p').get_text(strip=True)}
    return blog_dic

def get_medium_dict(url:str="https://medium.com/@p123456dan.mse99")->dict:
    a_tag = get_a_tag_from_url(url)
    a_tag_clean = get_raw_target_text(a_tag)
    blog_dic = gen_dict(a_tag_clean)
    return blog_dic