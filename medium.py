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

def gen_dict(raw:list)->dict:
    blog_dic = {}
    for url in raw:
        if url.find('h2'):
            try:
                partial_url = url['href'].split('?')[0]
                title = url.find('h2').get_text()
                content = url.find('h3').get_text()
                blog_dic[title]={'url':f'https://medium.com/{partial_url}', 'content':content}
            except:
                pass
    return blog_dic

def get_medium_dict(url:str="https://medium.com/@p123456dan.mse99")->dict:
    a_tag = get_a_tag_from_url(url)
    blog_dic = gen_dict(a_tag)
    return blog_dic