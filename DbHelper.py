import pymysql
import time
import configparser
import os


class DbHelper:
    config_path = os.path.dirname(__file__) + "/config.ini"
    conn = None
    @staticmethod
    def init_connect():
        print(DbHelper.config_path)
        conf = configparser.ConfigParser()
        conf.read(DbHelper.config_path)
        db_name = conf.get("db", "db_name")
        db_user = conf.get("db", "db_user")
        db_password = conf.get("db", "db_password")
        db_host = conf.get("db", "db_host")
        db_port = conf.get("db", "db_port")
        DbHelper.conn = pymysql.connect(host=db_host, port=int(db_port), user=db_user, password=db_password, database=db_name)

    @staticmethod
    def insert(table, user_name, target_name, message):
        try:
            cursor = DbHelper.conn.cursor()
            sql = "insert into " + table + " (user_name,target_name,content,ctime) value(%s,%s,%s,%s)"
            cursor.execute(sql, (user_name, target_name, message, int(time.time())))
            DbHelper.conn.commit()
            return True
        except Exception as e:
            print("发生异常", e)
            return False

    @staticmethod
    def get_all():
        try:
            cursor = DbHelper.conn.cursor()
            sql = "select * from chat_log order by ctime ASC"
            cursor.execute(sql)
            return cursor.fetchall()

        except Exception as e:
            print("发生异常", e)
            return False

    @staticmethod
    def close():
        DbHelper.conn.close()


#test
if __name__ == "__main__":
    DbHelper.init_connect()
    #DbHelper.insert("chat_log", "client", "server", "这是代码测试信息2")
    chat_list = DbHelper.get_all()
    for chat in chat_list:
        print(chat)
