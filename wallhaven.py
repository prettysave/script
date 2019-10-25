#!/usr/bin/env python
# coding:utf-8
import time

from bs4 import BeautifulSoup
import requests

URL_BASE = 'https://wallhaven.cc/toplist?page='
DOWNLOAD_PATH = "/Users/heyong/Pictures/%d.jpg"


def request_download(image_url, num):
    r = requests.get(image_url)
    with open(DOWNLOAD_PATH % num, 'wb') as f:
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
