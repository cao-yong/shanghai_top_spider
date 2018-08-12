# shanghai_top_spider数据爬虫
### 1.使用python3.7
### 2.框架Scrapy 1.5.1
### 3.数据保存到MySQL 5.7.23
### 4.数据定时一天更新一次
### 5.防止反爬使用代理
### 6.数据库脚本:
```sql
CREATE DATABASE /*!32312 IF NOT EXISTS*/`shanghai-top` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `shanghai-top`;

DROP TABLE IF EXISTS `top_site`;

CREATE TABLE `top_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `url` varchar(1024) DEFAULT NULL COMMENT '链接',
  `site_name` varchar(128) DEFAULT NULL COMMENT '地点名称',
  `site_id` varchar(128) DEFAULT NULL COMMENT '地点id',
  `star` int(11) DEFAULT NULL COMMENT '星级',
  `region_name` varchar(128) DEFAULT NULL COMMENT '所在区域名称',
  `category_name` varchar(64) DEFAULT NULL COMMENT '类别名称',
  `address` varchar(512) DEFAULT NULL COMMENT '地址',
  `img_url` varchar(2048) DEFAULT NULL COMMENT '图片url',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '修改时间',
  `sort` int(11) DEFAULT NULL COMMENT '序号',
  `is_deleted` char(1) DEFAULT 'N' COMMENT '是否删除（Y：是，N：否）',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
```