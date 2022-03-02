import sqlite3 as sql

# Datenbanken

# try:
#     conn = sql.connect("database.sqlite3")
# except sql.Error as e:
#     print(e)

# with sql.connect("database.sqlite3") as conn:
conn = sql.connect("database.sqlite3")
c = conn.cursor()
# c.execute("drop Table Test")
c.execute("create Table if not exists Test (x int ,y int ,z int)")
valueOne = 1
valueTwo = 2
valueThree = 3
# c.execute("insert into test values (?, ?, ?)", (valueOne, valueTwo, valueThree))
c.execute(f"insert into test values ({valueOne}, {valueTwo}, {valueThree})")
numberList = [
    (4, 5, 6),
    (7, 8, 9),
    (10, 11, 12),
    (13, 14, 15)
]
c.executemany("Insert into test values (?, ?, ?)", numberList)
c.executemany("Insert into test values (?, ?, ?)", numberList)
c.executemany("Insert into test values (?, ?, ?)", numberList)
c.execute("select * from test")
allRows = list(c)
print(allRows)
x = allRows[1]
x = list(x)
x[1] = 12
print(x)
allRows[1] = tuple(x)
print(allRows)
c.execute("Select rowid from test where x = 4")
index = c.fetchone()
print(index)
c.execute(f"update test set y={x[1]} where rowid ={index[0]}")
# c.execute("delete from test")
# c.executemany("insert into test values (?,?,?)", allRows)
conn.commit()  # Ohne commit werden die Daten nicht abgespeichert
# Mit with aber unnötig
# conn.close()

# with nutzt erst open und am ende des with-Blocks wird commit() und danach close() aufgerufen
