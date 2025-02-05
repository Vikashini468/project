from flask import Flask,render_template,request
from database import Database
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/home")
def home():
    db=Database()
    students=db.getAllUsers()
    return render_template("home.html",students=students)
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]
        print(email,password)
        db=Database()
        user=db.auth(email,password)
        if user:
            return '<script>alert("login Successfully....!");location.href="/home";</script>'
        else:
            return '<script>alert("login failed....!");location.href="/login";</script>'

@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=="GET":
        return render_template("signup.html")
    if request.method=="POST":
        id=request.form["id"]
        name=request.form["name"]
        dept = request.form["dept"]
        year = request.form["year"]
        email = request.form["email"]
        password = request.form["password"]
        print(id,name,dept,year,email,password)
        db=Database()
        db.addStudent(id,name,dept,year,email,password)
        return '<script>alert("signup Successfully....!");location.href="/login";</script>'

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=80)
