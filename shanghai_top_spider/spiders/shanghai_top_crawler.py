import random

import scrapy
from scrapy.http import Request

from shanghai_top_spider.items import ShanghaiTopSpiderItem
from user_agent import agents


class ShanghaiTopCrawler(scrapy.Spider):
    name = "shanghai_top_spider"
    allowed_domains = ["dianping.com"]
    start_urls = [
        # "http://www.dianping.com/search/keyword/1/0_%E6%99%AF%E7%82%B9/o2",
        # "http://www.dianping.com/search/keyword/1/0_%E5%95%86%E5%9C%88/o2",
        # "http://www.dianping.com/search/keyword/1/0_%E5%B0%8F%E5%90%83%E8%A1%97/o2"
        "file:///C:/Users/17092/Desktop/Untitled2.html"
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
            yield Request(url, callback=self.parse, headers=header)

    def parse(self, response):
        self.logger.info('the url is :%s', response.url)
        if response.status == 200:
            hxs = scrapy.Selector(response)
            xs = hxs.xpath('//*[@id="shop-all-list"]/ul/li')
            for x in xs:
                storage_item = ShanghaiTopSpiderItem()
                site_name = x.xpath('div[2]/div[1]/a[1]/h4/text()').extract()
                url = x.xpath('div[2]/div[1]/a[1]/@href').extract()
                site_id = x.xpath('div[2]/div[1]/a[1]/@data-shopid').extract()
                star = x.xpath('div[2]/div[2]/span/@title').extract()
                region_name = x.xpath('div[2]/div[3]/a[2]/span/text()').extract()
                category_name = x.xpath('div[2]/div[3]/a[1]/span/text()').extract()
                address = x.xpath('div[2]/div[3]/span/text()').extract()
                img_url = x.xpath('div[1]/a/img/@src').extract()

                storage_item['site_name'] = site_name
                storage_item['url'] = url
                storage_item['site_id'] = site_id
                storage_item['star'] = star
                storage_item['region_name'] = region_name
                storage_item['category_name'] = category_name
                storage_item['address'] = address
                storage_item['img_url'] = img_url
                yield storage_item
            else:
                return ''
