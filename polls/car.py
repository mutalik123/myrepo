from django.http import HttpResponse
import sqlite3
conn=sqlite3.connect('db.sqlite3')
c=conn.cursor()
class myone():
    def craete(self):
        c.execute("""create table emp(name varchar(20),age int,address char(50),sex char)""")
        c.execute("""insert into emp values('harish',25,'bangalore','M')""")
        c.execute("""select name,age,address,sex from emp""")

