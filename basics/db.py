import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

# cur.execute("CREATE TABLE movie(title, year, score)")
# cur.execute("CREATE TABLE students(student_id, student_name, student_phone)")

# cur.execute("INSERT INTO movie VALUES ('PRISONERS', '2000', '9')")
# cur.execute("INSERT INTO movie VALUES ('PRISONERS', '2025', '7.5')")

# cur.execute("DELETE FROM movie WHERE ")    



# cur.execute("DELETE FROM movie WHERE year = '2000'")


cur.execute("""
            UPDATE movie
            SET year = 1996
            WHERE title = 'forrest gumb'
            """)

res = cur.execute("SELECT * FROM movie")


con.commit()


print(res.fetchall())