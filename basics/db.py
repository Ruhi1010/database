import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

# cur.execute("CREATE TABLE movie(title, year, score)")
# cur.execute("CREATE TABLE students(student_id, student_name, student_phone)")

res = cur.execute("SELECT * FROM movie")

print(res.fetchall())