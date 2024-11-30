import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

# cur.execute("CREATE TABLE movie(title, year, score)")
# cur.execute("CREATE TABLE students(student_id, student_name, student_phone)")

# cur.execute("INSERT INTO movie VALUES ('PRISONERS', '2000', '9')")
# cur.execute("INSERT INTO movie VALUES ('PRISONERS', '2025', '7.5')")

# cur.execute("DELETE FROM movie WHERE ")    



# cur.execute("DELETE FROM movie WHERE year = '2000'")


# cur.execute("""
#             UPDATE movie
#             SET year = 1996
#             WHERE title = 'forrest gumb'
#             """)

# cur.execute("CREATE TABLE student(s_id, s_name, address, s_phone, s_blood_group)")

# cur.execute("INSERT INTO student VALUES ('01', 'AMIT', 'NARINDA', '01533610325', 'A-')")

# cur.execute("INSERT INTO student VALUES ('01', 'PLABON', 'AHMEDBAGH', '01533610183', 'B+')")

# cur.execute("DELETE FROM student WHERE s_id = '01'")

# cur.execute("""
#             UPDATE student 
#             SET s_id = '02'
#             WHERE s_name = 'AMIT'
#             """)

# cur.execute("""
#             CREATE TABLE IF NOT EXISTS student(
#                 s_id integer,
#                 s_name text,
#                 address text,
#                 s_phone text,
#                 s_blood_group text,
#                 PRIMARY KEY (s_id, s_phone)
#             )
#             """)



# cur.execute("INSERT INTO student VALUES ('03', 'RAKIB', 'MUGDA', '01533610185', 'AB+')")

# cur.execute("CREATE TABLE employee('name', 'age', 'salary', 'department', 'ID')")

# cur.execute("INSERT INTO employee VALUES ('Ruhi', '22', '500000', 'HR', '01')")

# cur.execute("INSERT INTO employee VALUES ('Rakib', '23', '200000', 'ADMIN', '01')")

# cur.execute("""
#             UPDATE employee
#             SET department = 'IT'
#             WHERE name = 'Rakib'
#             """)

# cur.execute("""
#             INSERT INTO employee VALUES
#             ('Rishat', '30', '100000', 'IT', '03'),
#             ('Rahim', '25', '80000', 'HR', '05'),
#             ('Rana', '27', '70000', 'ADMIN', '04')
#             """)

# cur.execute("DELETE FROM employee WHERE ID = '05'")


# cur.execute("ALTER TABLE employee RENAME TO old_employee")


# cur.execute("CREATE TABLE employee(name, age, salary, department, ID PRIMARY KEY)")


# cur.execute("INSERT INTO employee SELECT * FROM old_employee")


# cur.execute("DROP TABLE old_employee")

cur.execute("INSERT INTO employee VALUES('Karim', '30', '850000', 'HR', '01')")


res = cur.execute("SELECT * FROM employee")


print(res.fetchall())


con.commit()