# -*- coding: utf-8 -*-

import MySQLdb

class Database(object):

    def __init__(self, db, host='localhost', port=3306, user='root', passwd='root'):
        self.__host = host
        self.__port = port
        self.__db = db
        self.__user = user
        self.__passwd = passwd
        try:
            self.__conn = MySQLdb.connect(host, user, passwd, db, port)
            self.__cur = self.__conn.cursor()
        except MySQLdb.Error, e:
            print("connect MySQL fail %d" % e.args[0])
            raise MySQLdb.Error

    """ 创建数据库 """
    def __createDB(self):
        try:
            self.__cur.execute("CREATE DATABASE %s IF NOT EXISTS" % self.__db)
        except MySQLdb.Error, e:
            print("CREATE DATABASE fail %d" % e.args[0])




