# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors
from twisted.enterprise import adbapi


class ShanghaiTopSpiderPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings['MYSQL_HOST'],  # 读取settings中的配置
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)  # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        return cls(dbpool)  # 相当于dbpool付给了这个类，self中可以得到

    # pipeline默认调用
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
        query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        return item

    # 写入数据库中
    count = 0

    def _conditional_insert(self, tx, item):
        # print item['name']
        # sql="insert into testtable(name,url) values(%s,%s)"
        # 需要插入到数据库的字段和相应的值
        sql = "INSERT INTO `shanghai-top`.`top_site`(`url`,`site_name`,`site_id`,`star`," \
              "`region_name`,`category_type`,`category_name`,`address`,`img_url`,`create_time`,`update_time`," \
              "`sort`,`is_deleted`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW(),NOW(),%s,'N')"
        params = (item["url"], item["site_name"], item["site_id"], item["star"], item["region_name"],
                  item["category_type"], item["category_name"], item["address"], item["img_url"], item["sort"])
        tx.execute(sql, params)
        self.count = self.count + 1
        print('成功插入 %s 条数据到数据库' % self.count)

    # 错误处理方法
    def _handle_error(self, failue, item, spider):
        print('--------------database operation exception!!-----------------')
        print('-------------------------------------------------------------')
        print(failue)
