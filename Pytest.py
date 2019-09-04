import pymysql


class Pytest():
    def __init__(self,host,user,passwd,dbName):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.dbName = dbName

    def connect(self):
        self.db =pymysql.connect(self.host,self.user,self.passwd,self.dbName)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self,sql):
        res = None

        self.connect()
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        self.close()

        return res


