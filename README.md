# database
 
## How to create a database in SQLite3

**format**:
```python
import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

cur.execute("CREATE TABLE movie(title, year, score)")

res = cur.execute("SELECT * FROM movie")

res.fetchall()
```

## How to create a table in SQLite3
```SQL
CREATE TABLE table_name(column 1, column 2, column3,.....)
```