import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.0.102",
  user="priyanshu",
  password="1234",
  database="teacher_t1"
)

data = mydb.cursor()
data.execute("show tables")

for i in data:
    print(i)

