/*
 Navicat Premium Data Transfer

 Source Server         : ZzhirenMac
 Source Server Type    : MySQL
 Source Server Version : 50722
 Source Host           : localhost:3306
 Source Schema         : blog

 Target Server Type    : MySQL
 Target Server Version : 50722
 File Encoding         : 65001

 Date: 16/04/2019 15:07:41
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `id` int(11) NOT NULL,
  `author_id` int(11) DEFAULT NULL COMMENT '作者id，创建文章的用户id',
  `title` varchar(255) NOT NULL COMMENT '文章标题',
  `keywords` varchar(255) NOT NULL COMMENT '关键字',
  `preface` varchar(255) NOT NULL COMMENT '文章前言',
  `content` longtext NOT NULL COMMENT '文章内容',
  `thumb_url` varchar(255) NOT NULL COMMENT '缩略图url',
  `source` int(255) NOT NULL DEFAULT '1' COMMENT '文章来源：1-原创，2-转载',
  `status` int(255) NOT NULL DEFAULT '1' COMMENT '文章发布状态：1-直接发布，2-草稿',
  `publicity` int(255) NOT NULL DEFAULT '1' COMMENT '是否公开：1-公开，2-未公开',
  `locking` int(255) NOT NULL DEFAULT '1' COMMENT '锁定文章：1-未锁定，2-锁定',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `fk_article` (`author_id`),
  CONSTRAINT `fk_article` FOREIGN KEY (`author_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='文章表';

-- ----------------------------
-- Table structure for article_relate_classify
-- ----------------------------
DROP TABLE IF EXISTS `article_relate_classify`;
CREATE TABLE `article_relate_classify` (
  `id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL COMMENT '文章id',
  `classify_id` int(11) NOT NULL COMMENT '分类id',
  PRIMARY KEY (`id`),
  KEY `fk_article_relate_classify` (`article_id`),
  KEY `fk_article_relate_classify_1` (`classify_id`),
  CONSTRAINT `fk_article_relate_classify` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_article_relate_classify_1` FOREIGN KEY (`classify_id`) REFERENCES `classify` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for article_relate_label
-- ----------------------------
DROP TABLE IF EXISTS `article_relate_label`;
CREATE TABLE `article_relate_label` (
  `id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL COMMENT '文章id',
  `label_id` int(11) NOT NULL COMMENT '标签id',
  PRIMARY KEY (`id`),
  KEY `fk_article_relate_label_article_1` (`article_id`),
  KEY `fk_article_relate_label_label_1` (`label_id`),
  CONSTRAINT `fk_article_relate_label_article_1` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `fk_article_relate_label_label_1` FOREIGN KEY (`label_id`) REFERENCES `label` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='文章-标签-关联表';

-- ----------------------------
-- Table structure for classify
-- ----------------------------
DROP TABLE IF EXISTS `classify`;
CREATE TABLE `classify` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL COMMENT '分类名称',
  `icon_url` varchar(255) NOT NULL COMMENT '图标地址',
  `description` varchar(255) DEFAULT NULL COMMENT '描述',
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL,
  `article_id` int(11) DEFAULT NULL COMMENT '文章id',
  `nick_name` varchar(255) NOT NULL COMMENT '昵称',
  `content` mediumtext NOT NULL COMMENT '评论内容',
  `selection` int(255) NOT NULL DEFAULT '1' COMMENT '是否精选：1-未精选（默认值），2-精选',
  `status` int(255) NOT NULL DEFAULT '1' COMMENT '状态：1-未放入回收站，2-已放入回收站',
  `create_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  `readed` int(11) NOT NULL COMMENT '1-未读，2-已读，未读将会在通知中显示',
  PRIMARY KEY (`id`),
  KEY `fk_comment` (`article_id`),
  CONSTRAINT `fk_comment` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for comment_reply
-- ----------------------------
DROP TABLE IF EXISTS `comment_reply`;
CREATE TABLE `comment_reply` (
  `id` int(11) NOT NULL,
  `comment_id` int(11) DEFAULT NULL,
  `nick_name` varchar(255) NOT NULL COMMENT '昵称',
  `reply_to` varchar(255) DEFAULT NULL COMMENT '回复的对象（昵称）',
  `content` mediumtext NOT NULL COMMENT '回复内容',
  `status` int(255) NOT NULL DEFAULT '1' COMMENT '屏蔽状态：1-未屏蔽，2-屏蔽',
  `create_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `f_comment_reply` (`comment_id`),
  CONSTRAINT `f_comment_reply` FOREIGN KEY (`comment_id`) REFERENCES `comment` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for label
-- ----------------------------
DROP TABLE IF EXISTS `label`;
CREATE TABLE `label` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL COMMENT '标签名称',
  `icon_url` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL COMMENT '描述',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='标签表';

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `account` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL COMMENT '用户姓名',
  `email` varchar(255) DEFAULT NULL COMMENT '邮箱',
  `nick_name` varchar(255) NOT NULL COMMENT '昵称',
  `age` int(255) DEFAULT NULL COMMENT '年龄',
  `hight` double(255,0) DEFAULT NULL COMMENT '身高',
  `weight` double(255,0) DEFAULT NULL COMMENT '体重',
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

SET FOREIGN_KEY_CHECKS = 1;
