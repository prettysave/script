#!/usr/bin/env python
# coding:utf-8
import time

from bs4 import BeautifulSoup
import requests
import os

URL_BASE = 'https://wallhaven.cc/toplist?page='


def request_download(IMAGE_URL, num):
    r = requests.get(IMAGE_URL)
    path = "/Users/heyong/Pictures/%d.jpg" % num
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close()
        print('success:%d.jpg' % num)


def get_download_url(preview_url):
    r = requests.get(preview_url)
    html = r.text

    bf = BeautifulSoup(html, 'html.parser')
    texts = bf.find_all('img', id='wallpaper')

    links = []
    for link in texts:
        links.append(link.get('src'))

    return links


def get_preview_url(page_num):
    req = requests.get(url=URL_BASE + str(page_num))
    html = req.text

    bf = BeautifulSoup(html, 'html.parser')
    texts = bf.find_all('a', class_='preview')

    links = []
    for link in texts:
        links.append(link.get('href'))

    return links


if __name__ == '__main__':
    i = 1
    number = 1
    while i <= 3:
        time.sleep(0.5)
        preview_links = get_preview_url(i)
        for preview_link in preview_links:
            time.sleep(0.5)
            download_links = get_download_url(preview_link)
            for download_link in download_links:
                time.sleep(1)
                request_download(download_link, number)
                number += 1
        i += 1

    # request_download('https://w.wallhaven.cc/full/6k/wallhaven-6ky6dq.jpg', 1)
    # get_preview_url('https://wallhaven.cc/w/oxj8zm')
    # target = 'https://wallhaven.cc/'
    # url1 = 'https://wallhaven.cc/toplist'
    # url2 = 'https://wallhaven.cc/toplist?page=2'
    # url3 = 'https://wallhaven.cc/w/oxj7mm'
    #
    # req = requests.get(url=url2)
    #
    # html = req.text
    # texts = req.text
    #
    # bf = BeautifulSoup(html, 'html.parser')
    #
    # texts = bf.find_all('a', class_='preview')
    # texts = bf.find_all('div', id='overlay')
    # for link in texts:
    #     print(link.get('href'))

    # print(texts)
    # print(texts[0].text.replace('\xa0' * 8, '\n\n'))
