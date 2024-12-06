import sqlite3
con = sqlite3.connect("class_work.db")

cur = con.cursor()

# Question 1 

# cur.execute("CREATE TABLE Employees(EmployeeID PRIMARY KEY, Name, Position, Salary)")
# cur.execute("""
#             INSERT INTO Employees VALUES('1', 'Alice', 'Manager', '80000'),
#             ('2', 'Bob', 'Developer', '60000'),
#             ('3', 'Charlie', 'Tester', '40000'),
#             ('4', 'Diana', 'Developer', '60000')         
#             """)
# cur.execute("INSERT INTO Employees VALUES('5', 'Eve', 'HR', '50000')")


# cur.execute("""
#             UPDATE Employees
#             SET Salary = '60000'
#             WHERE Position = 'Developer'
#             """)











# Question 2
# cur.execute("CREATE TABLE Products(ProductID PRIMARY KEY, ProductName, Category, Price, Stock)")
# cur.execute("""
#             INSERT INTO Products VALUES('1', 'Laptop', 'Electronics', '1000','50'),
#             ('2', 'Chair', 'Furniture', '150', '200'),
#             ('3', 'Smartphone', 'Electronics', '800', '30'),
#             ('4', 'Desk', 'Furniture', '300', '100')         
#             """)


# res = cur.execute("SELECT * FROM Products WHERE Category = 'Electronics' AND Price>500")


# cur.execute("""
#             UPDATE Products
#             SET Stock = '40'
#             WHERE ProductName = 'Laptop'
#             """)


# cur.execute("DELETE FROM Products WHERE Stock = '100' AND Category = 'Furniture'")





# Question 3
# cur.execute("CREATE TABLE Students(StudentID PRIMARY KEY, Name, Course, Grade)")
# cur.execute("""
#             INSERT INTO Students VALUES('1', 'John', 'Mathematics', 'B'),
#             ('2', 'Sarah', 'Physics', 'A'),
#             ('3', 'Michael', 'Chemistry', 'C'),
#             ('4', 'Anna', 'Mathematics', 'A')         
#             """)

# res = cur.execute("SELECT * FROM Students WHERE Course = 'Mathematics' AND Grade = 'A'")

# cur.execute("INSERT INTO Students VALUES('5', 'Emily', 'Biology', 'B')")

# cur.execute("""
#             UPDATE Students
#             SET Grade = 'B'
#             WHERE Name = 'Michael' AND Course = 'Chemistry'
#             """)






# res = cur.execute("SELECT AVG(Salary) FROM Employees WHERE Position = 'Developer'")
res = cur.execute("SELECT * FROM Students")


print(res.fetchall())


con.commit()