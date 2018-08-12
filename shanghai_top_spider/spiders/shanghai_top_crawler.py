import random

import scrapy
from bs4 import BeautifulSoup as bs
from scrapy.http import Request

from shanghai_top_spider.items import ShanghaiTopSpiderItem
from user_agent import agents
from user_agent import proxies


class ShanghaiTopCrawler(scrapy.Spider):
    name = "shanghai_top_spider"
    allowed_domains = ["dianping.com"]
    start_urls = [
        "http://www.dianping.com/search/keyword/1/0_%E6%99%AF%E7%82%B9/o2",
        "http://www.dianping.com/search/keyword/1/0_%E5%95%86%E5%9C%88/o2",
        "http://www.dianping.com/search/keyword/1/0_%E5%B0%8F%E5%90%83%E8%A1%97/o2"
    ]

    def start_requests(self):
        for url in self.start_urls:
            header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip,deflate,sdch',
                'Accept-Language': 'zdeprecatedh-CN,zh;q=0.8,en;q=0.6',
                'Host': 'www.dianping.com',

                'User-Agent': random.choice(agents),
                'Referer': url,
            }
            yield Request(url, callback=self.parse, headers=header, meta={'proxy': 'http://' + random.choice(proxies)})

    def parse(self, response):
        self.logger.info('the url is :%s', response.url)
        if response.status == 200:
            soup = bs(response.text, 'html.parser')
            # 获取主要内容并去掉广告

            main_content = soup.select('#shop-all-list')
            index = 1
            for content in main_content:
                site_name = content.select('ul > li:nth-child(' + str(index) + ') > div.txt > div.tit > a > h4');
                storage_item = ShanghaiTopSpiderItem()
                storage_item['site_name'] = site_name
                index += 1
