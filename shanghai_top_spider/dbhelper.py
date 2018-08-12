# import MySQLdb
import pymysql
from scrapy.utils.project import get_project_settings


class DBHelper:

    def __init__(self):
        # 配置在config.py中的数据库信息
        self.settings = get_project_settings()
        self.host = self.settings['MYSQL_HOST']
        self.port = self.settings['MYSQL_PORT']
        self.user = self.settings['MYSQL_USER']
        self.passwd = self.settings['MYSQL_PASSWD']
        self.db = self.settings['MYSQL_DBNAME']

    def connect_mysql(self):
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               charset='utf8')
        return conn

    def connect_database(self):
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               db=self.db,
                               charset='utf8')
        return conn

    def create_database(self):
        conn = self.connect_mysql()

        sql = "create database if not exists " + self.db
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()

    def create_table(self, sql):
        conn = self.connect_database()
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()

    def insert(self, sql, *params):
        conn = self.connect_database()

        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()

    def update(self, sql, *params):
        conn = self.connect_database()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()

    def delete(self, sql, *params):
        conn = self.connect_database()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()


class TestDBHelper:
    def __init__(self):
        self.dbHelper = DBHelper()

    def test_create_database(self):
        self.dbHelper.create_database()

    def test_create_table(self):
        sql = "CREATE TABLE `top_site` (`id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',`url`" \
              " varchar(1024) DEFAULT NULL COMMENT '链接',`site_name` varchar(128) DEFAULT NULL" \
              " COMMENT '地点名称',`site_id` varchar(128) DEFAULT NULL COMMENT '地点id',`star` int(11) " \
              "DEFAULT NULL COMMENT '星级',`region_name` varchar(128) DEFAULT NULL COMMENT '所在区域名称'," \
              "`category_name` varchar(64) DEFAULT NULL COMMENT '类别名称',`address` varchar(512) DEFAULT NULL " \
              "COMMENT '地址',`img_url` varchar(2048) DEFAULT NULL COMMENT '图片url',`create_time` datetime DEFAULT NULL" \
              " COMMENT '创建时间',`update_time` datetime DEFAULT NULL COMMENT '修改时间',`sort` int(11) DEFAULT NULL" \
              " COMMENT '序号',`is_deleted` char(1) DEFAULT 'N' COMMENT '是否删除（Y：是，N：否）',PRIMARY KEY (`id`)) " \
              "ENGINE=InnoDB DEFAULT CHARSET=utf8"
        self.dbHelper.create_table(sql)

    def test_insert(self):
        sql = "INSERT INTO `shanghai-top`.`top_site`(`url`,`site_name`,`site_id`,`star`," \
              "`region_name`,`category_name`,`address`,`img_url`,`create_time`,`update_time`," \
              "`sort`,`is_deleted`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,NOW(),NOW(),%s,'N')"
        params = ("x", "x", "x", "1", "x", "x", "x", "x", "1")
        self.dbHelper.insert(sql, *params)

    def test_update(self):
        sql = "UPDATE `shanghai-top`.`top_site` SET `url`=%s,`site_name`=%s,`site_id`=%s WHERE `id`='1'"
        params = ("zz", "zz", "zz")
        self.dbHelper.update(sql, *params)

    def test_delete(self):
        sql = "DELETE FROM `shanghai-top`.`top_site`  WHERE `id`=%s"
        params = "1"
        self.dbHelper.delete(sql, *params)


if __name__ == "__main__":
    testDBHelper = TestDBHelper()
    # testDBHelper.test_update()
