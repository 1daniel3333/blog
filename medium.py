from bs4 import BeautifulSoup
import urllib.request

def get_a_tag_from_url(url:str="https://medium.com/@p123456dan.mse99"):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        html_bytes = response.read()  # Fetch the HTML content as bytes
        html_str = html_bytes.decode("utf-8")  # Convert bytes to a string
        soup = BeautifulSoup(html_str, "html.parser")  # Create a Beautiful Soup object
        a_tags = soup.find_all('a')

    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
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