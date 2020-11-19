import requests
from bs4 import BeautifulSoup
'''
返回一个网址列表，网址指向单个文章
'''
def get_urls():
    # 网址列表：目录的网址
    source_urls = []
    target_urls = []
    for i in range(1, 17):
        source_urls.append('http://opinion.people.com.cn/GB/8213/49160/49219/index'+ str(i) +'.html')

    for source_url in source_urls:
        res = requests.get(source_url)
        res.encoding = 'gbk'
        html_doc = res.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        prefix = 'http://opinion.people.com.cn'
        select_result = soup.select('.abl')
        for i in range(len(select_result)):
            target_url = prefix + select_result[i].attrs['href']
            if '2020' not in target_url:
                break
            target_urls.append(target_url)
    
    return target_urls
