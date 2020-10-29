# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

'''
params: url
return: dict {title, content array}
'''
def get_article(url):
    # url = 'http://opinion.people.com.cn/n1/2020/1028/c1003-31908449.html'
    res = requests.get(url)
    res.encoding = 'GBK'
    html_doc = res.text

    title_content_dict = {}
    try:
        soup = BeautifulSoup(html_doc, 'html.parser')
        title = soup.select('body > div.clearfix.w1000_320.text_title > h1')[0].get_text()
        content = soup.select('#rwb_zw')[0].get_text()
        content_arr = content.split()
            
        title_content_dict['title'] = title.split('：')[-1]
        title_content_dict['content_arr'] = []
        for i in range(len(content_arr)):
            if content_arr[i] == '《' and content_arr[i+1] == '人民日报':
                break
            if content_arr[i].find('责编：') == -1:
                title_content_dict['content_arr'].append(content_arr[i])
    except IndexError:
        raise IndexError

    return title_content_dict

    