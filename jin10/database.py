# -*- coding: utf-8 -*-

import MySQLdb
from time import *


class Database(object):
    def __init__(self, db, host='localhost', port=3306, user='root', passwd='tang85718'):
        self.__host = host
        self.__port = port
        self.__db_name = db
        self.__user = user
        self.__passwd = passwd
        try:
            self.__conn = MySQLdb.connect(host, user, passwd, db, port)
            self.__cur = self.__conn.cursor()
            self.__create_db()
            self.__create_raw_table()
        except MySQLdb.Error, e:
            print("connect MySQL fail %d" % e.args[0])

    """ 创建数据库 """

    def __create_db(self):
        try:
            self.__cur.execute("CREATE DATABASE `spider`")
        except MySQLdb.Error, e:
            print("CREATE DATABASE fail %d" % e.args[0])

    def __create_raw_table(self):
        try:
            self.__cur.execute("CREATE TABLE `raw_data` ("
                               "`id` INT(11) NOT NULL AUTO_INCREMENT,"
                               "`content` TEXT NOT NULL,"
                               "`create_time` DATETIME NOT NULL,"
                               "PRIMARY KEY (`id`))"
                               "ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8")

        except MySQLdb.DatabaseError, e:
            print("create table spider failure %d" % e.args[0])

    def create_or_update(self, mid, content):
        try:
            date = strftime("%Y-%m-%d %H:%M:%S", localtime())
            insert_sql = "INSERT INTO spider.raw_data (`mid`,`content`,`create_time`)" \
                         "SELECT '%d','%s','%s' FROM dual " \
                         "WHERE NOT EXISTS" \
                         "(SELECT mid FROM spider.raw_data WHERE mid=%d)" % (mid, content, date, mid)
            # print(insert_sql)

            self.__cur.execute(insert_sql)
            self.__conn.commit()
        except MySQLdb.DatabaseError, e:
            print("create_or_update Error: %d" % e.args[0])
            self.__conn.rollback()
