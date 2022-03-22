import mysql.connector
from dbutils.pooled_db import PooledDB
import os
from dotenv import load_dotenv

load_dotenv(".env")

pool=PooledDB(
    creator=mysql.connector.connect,
    mincached=2,
    maxcached=5,
    maxconnections=20,
    blocking=True,
    host=os.getenv("host"),
    port=os.getenv("port"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    database=os.getenv("database"),
)
try:
    connection=pool.connection()
    cursor=connection.cursor()

except:
    print("連線資料庫失敗！")
finally:
    cursor.close()
    connection.close()

