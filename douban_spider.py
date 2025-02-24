import requests
import csv
import time
import random
from lxml import etree

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}
data = []
for i in range(10):
    sleep_time = random.randint(1, 2) + random.random()
    time.sleep(sleep_time)
    url = f'https://movie.douban.com/top250?start={i*25}&filter='
    res = requests.get(url=url,headers=headers)

    tree = etree.HTML(res.text)
    lis = tree.xpath('/html/body/div[3]/div[1]/div/div[1]/ol/li')
    for li in lis:
        dic = []
        name = li.xpath('.//div/div[2]/div[1]/a/span[1]/text()')
        dic.append(name[0] if name else '')

        score = li.xpath('.//div/div[2]/div[2]/div/span[2]/text()')
        dic.append(score[0] if score else '')
        num = li.xpath('.//div/div[2]/div[2]/div/span[4]/text()')
        dic.append(num[0].split('人评价')[0] if num else '')
        pingyu = li.xpath('.//div/div[2]/div[2]/p[2]/span/text()')
        dic.append(pingyu[0] if pingyu else '')
        daoyan = li.xpath('.//div/div[2]/div[2]/p[1]/text()[1]')[0].strip().split('导演: ')[1].split('主演: ')[0]
        dic.append(daoyan)
        info = li.xpath('.//div/div[2]/div[1]/a/@href')
        dic.append(info[0] if info else '')
        data.append(dic)

with open('豆瓣电影Top250.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['电影名称', '评分', '评价数', '影评', '导演', '详情链接'])
    writer.writerows(data)
