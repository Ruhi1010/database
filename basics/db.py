import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

# cur.execute("CREATE TABLE movie(title, year, score)")
# cur.execute("CREATE TABLE students(student_id, student_name, student_phone)")

cur.execute("INSERT INTO movie VALUES ('PRISONERS', '2000', '9')")

res = cur.execute("SELECT * FROM movie")

con.commit()


print(res.fetchall())