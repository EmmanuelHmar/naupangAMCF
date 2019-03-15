import sqlite3 as lite
import sys
import random

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
