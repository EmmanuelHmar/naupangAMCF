import sqlite3 as lite
from sqlite3 import Error
import sys
import random


def create_connection(db_file):
    #create a connection to the database file
    try:
        con = lite.connect(db_file)
        print("Opened db from Main")
        return con
    except Error as e:
        print(e)
    
    return None

def select_all_zirtirtu(con):
    cur = con.cursor()
    cur.execute("SELECT * From ZIRTIRTU")


# TODO: need to reset the counter to 0 when all teachers have had their turn
    rows = cur.fetchall()

    turnLimit = 0;
    zirtirtu = rows[0] 

    for row in rows:
        if (row[3]!=0):
            zirtirtu = row
            turnLimit = turnLimit - 1
        print(row)

    #while rows[3] != 1:
    #        zirtirtu = rows[0]#random.choice(rows)


    count = 0 if zirtirtu[3] == 1 else 1

    print('Thawhlawm Hlantu - ' + zirtirtu[1])
    print(count)

    cur.execute('''UPDATE ZIRTIRTU SET COUNT = ? WHERE NAME = ? ''',
            (count,zirtirtu[1]))

    rows = cur.fetchall()
    for row in rows:
        print(row)


    if (turnLimit == 0):
        for x in rows:
            cur.execute('''UPDATE ZIRTIRTU SET COUNT = ? WHERE NAME = ? ''',
            (0,x[1]))

    cur.close()

    

'''
con = lite.connect('db.db')

cursor = con.cursor()

print("Opened db from Main")

juniorDept = ['Lalrinsanga','Andrew Rampana','Juliana Vanlalhlimpuii','Melody Malsawmhlui ']

primaryDept = ['Elizabeth Lalawmpuii','Caleb Lalrinliana','Joseph Rinmawia']

beginnerDept = ['Jayson Lalrammawia','Joel Vanlalrinmuana','Esther Lalrinliani','Kristy Rinmawii']

zirtirtu = ['Pi Machhuani','Lalremruati','Lalrawngbawla']

dept = ['Pi Machhuani[Junior]','Lalremruati[Primary]','Lalrawngbawla[Junior']

chairperson = '1. Chairperson : ' #Junior Dept
inkhawmHlan = '2. Inkhawm hlan tawngtaitu : '
bibleChhiar = '3. Bible chhiartu : ' #Junior Dept #Primary Dept
thilPekKhawntu = '4. Thilpek khawntu : Joel Vanlalrinmuana (Beginner Dept)' #Beginner Dept
thawhHlawmHlantu = '5. Thawhlawm hlan tawngtaitu: ' #Zirtirtu
solo = '6. Solo - '
attendance = '7. Attendance - Hming lamna'
lalBiakSawi = '8. Lal biakna sawi rual'

print(chairperson + random.choice(juniorDept))
print(inkhawmHlan + random.choice(primaryDept))
print(bibleChhiar + random.choice(beginnerDept))
'''

def main():
    database = 'db.db'

    con = create_connection(database)

    with con:
        print("Testing zirtirtu")
        select_all_zirtirtu(con)


    

if __name__ == '__main__':
    main()