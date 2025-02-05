import mysql.connector
class Database:
    def __init__(self):
        self.conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="college"
        )
    def addStudent(self,id,name,dept,year,email,password):
        cur=self.conn.cursor()
        query="insert into student values(%s,%s,%s,%s,%s,%s)"
        values=(id,name,dept,year,email,password)
        cur.execute(query,values)
        self.conn.commit()
    def auth(self,email,password):
        cur = self.conn.cursor()
        query="select * from student where email=%s and password=%s"
        values=(email,password)
        cur.execute(query, values)
        user=cur.fetchone()
        return user
    def getAllUsers(self):
        cur=self.conn.cursor()
        query="select * from student"
        cur.execute(query)
        users=cur.fetchall()
        return users
        def deleteStudent(self,id):
        cur=self.conn.cursor()
        query="delete from student where id=%s"
        values=(id,)
        cur.execute(query,values)
        self.conn.commit()
