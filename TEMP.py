#!/usr/bin/python3
import requests
from lxml import etree

url = "https://movie.douban.com/top250"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}

html = requests.get(url, headers=headers).content.decode()

data = etree.HTML(html)
# 提取数据
movies = data.xpath('//span[@class="title"][1]/text()')
hrefs = data.xpath('//div[@class="hd"]/a/@href')
scores = data.xpath('//span[@class="rating_num"]/text()')
nums = data.xpath('//div[@class="star"]/span[4]/text()')

# xpath返回的都是列表格式
for a, b, c, d in zip(movies, hrefs, scores, nums):
    print("电影：%s，链接：%s，评分：%s，评论人数：%s" % (a, b, c, d))
