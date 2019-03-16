import sqlite3 as lite
import sys
import random

con = lite.connect('db.db')

cursor = con.cursor()

print("Opened db success")

cursor.execute('''CREATE TABLE NAUPANG 
    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    NAME TEXT NOT NULL,
    DEPARTMENT TEXT NOT NULL);''')

personSql = "INSERT INTO NAUPANG (NAME,DEPARTMENT) VALUES (?,?)"
cursor.execute(personSql,('Andrew Rampana','Junior Dept'))
cursor.execute(personSql,('Juliana Vanlalhlimpuii','Junior Dept'))

zirtirtuQuery = '''CREATE TABLE ZIRTIRTU 
    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    NAME TEXT NOT NULL,
    DEPARTMENT TEXT NOT NULL,
    COUNT INTEGER NOT NULL DEFAULT 0);'''

cursor.execute(zirtirtuQuery)

# Executeasmany
insertZirtirtu = "INSERT INTO ZIRTIRTU (NAME,DEPARTMENT) VALUES (?,?)"
cursor.execute(insertZirtirtu,('Lalrawngbawla','Junior Dept'))
cursor.execute(insertZirtirtu,('Pi Machhuani','Beginner Dept'))
cursor.execute(insertZirtirtu,('Lalremruati','Primary Dept'))


con.commit()
con.close()
