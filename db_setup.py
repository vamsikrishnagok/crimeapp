import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='apple')

try:
    with connection.cursor() as cursor:
        sql = " CREATE DATABASE IF NOT EXISTS crimeapp"
        cursor.execute(sql)
        sql = sql = """CREATE TABLE IF NOT EXISTS crimeapp.crimes (
id int NOT NULL AUTO_INCREMENT,
latitude FLOAT(10,6),
longitude FLOAT(10,6),
date DATETIME,
category VARCHAR(50),
description VARCHAR(1000),
updated_at TIMESTAMP,
PRIMARY KEY (id)
)"""
        cursor.execute(sql);
        connection.commit()
finally:
        connection.close()
