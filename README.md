# database_101


## How to create a database in SQLITE3

**format**:
```python

import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

cur.execute("CREATE TABLE movie(title, year, score)") 

res = cur.execute("SELECT * FROM movie")

res.fetchall()

```

## How to create a table in sqlite3

```SQL
CREATE TABLE table_name(column1, column2, column3, ...);
```

## How to insert data into a table in sqlite3

```SQL

INSERT INTO table_name VALUES (value1, value2, ..., valueN);

```


## how to set data types of a column in a table

```SQL

CREATE TABLE table_name(column1 INTEGER, column2 TEXT, column3 REAL);

```

`TEXT = string`
`INTEGER = integer`
`REAL = float`

> If the input is not of the correct type, it will be converted to the correct type.( for real and integer)
> But for text, if there are no quotes given, then it will not take the input in the table.

> If you input a string in an column of any kind or datatype, it wont be converted to the correct type, it will be stored as a string.

> If you input a numeric value with a quote in a numeric column, it will be converted in to the right column type.

## How to add a row permanently in a table

```python

import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

# cur.execute("CREATE TABLE movie(title TEXT, year INTEGER, score REAL)") 

cur.execute("INSERT INTO movie VALUES ('PRISONERS', '10', '9')")

res = cur.execute("SELECT * FROM movie") ## read all data from movie table

## we can add any datatype 
## not permanently stored

con.commit() # this will add the data into the database


print(res.fetchall())
    
```


## How to delete a row 
```SQL
DELETE FROM table_name WHERE column_name = value /* when the value is string then we put value in quotes*/
```

> Here the DELETE form command is used to tell the database that we want to delete a row from the table.

WHERE is the keyword for conditions, which is used to specify the condition for the rows to be deleted.


## How to update a value from a row 
```SQL
UPDATE table_name
SET column1 = value1, column2 = value2, ......, columnN = valueN
WHERE [Condition] /* Must check the condition very carefully*/
```

### How to take inputs in more than one rows
```SQL
cur.execute("""
            INSERT INTO table_name VALUES
            ('value1', 'value2',....,'valueN'),
            ('value1', 'value2',....,'valueN'),
            ('value1', 'value2',....,'valueN')
            """)
```