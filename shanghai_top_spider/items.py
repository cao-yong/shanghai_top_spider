# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShanghaiTopSpiderItem(scrapy.Item):
    # 链接
    url = scrapy.Field()
    # 地点名称
    site_name = scrapy.Field()
    # 地点id
    site_id = scrapy.Field()
    # 星级
    star = scrapy.Field()
    # 所在区域名称
    region_name = scrapy.Field()
    # 类别名称
    category_name = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 图片url
    img_url = scrapy.Field()