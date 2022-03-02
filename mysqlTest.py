import mysql.connector

db = mysql.connector.connect(
    host="",
    user="",
    port=3306,
    password="",
    database="pythontest220223"
)
print(db)
c = db.cursor()
c.execute("create table if not exists marius_test(name varchar(255), num int)")
c.execute("show tables")
for dbs in c:
    print(dbs)
