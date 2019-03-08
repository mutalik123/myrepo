import sqlite3
conn = sqlite3.connect('starlly1.db')
class demo:

    def create(self):
        c = conn.cursor()
        c.execute("""create table if not exists e(id int primary key,name char,age int,address char)""")
    def insert(self):
        c=conn.cursor()
        name=input("enter the name")
        age=input("enter the age")
        address=input("enter address")
        cnum=input("enter contact number")
        c.execute("""insert into e(name,age,address,cnum)values(?, ?, ?, ?)""",(name,age,address,cnum))
        print("inserted successfully")
    def ex(self):
        c=conn.cursor()
        c.execute("""select rowid,name,age,address,cnum from e""")
        for row in c:
            print("ID = ", row[0])
            print("name=", row[1])
            print("age=", row[2])
            print("address=", row[3])
            print("contact number", row[4])

obj=demo()
obj.create()
obj.insert()
obj.select()