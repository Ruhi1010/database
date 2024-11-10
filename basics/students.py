import sqlite3
con = sqlite3.connect("students.db")

cur = con.cursor()

cur.execute("CREATE TABLE students(student_id, student_name, student_mobile)")

res = cur.execute("SELECT * FROM movie")

res.fetchall()