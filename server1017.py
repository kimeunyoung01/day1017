from flask import Flask, render_template, request,redirect, url_for
import bitutil.stu

app = Flask(__name__)

@app.route("/insert", methods=['GET'])
def insertForm():
    return render_template("insertStudent.html")

@app.route("/insert", methods=['POST'])
def insert():
    name = request.form['name']
    kor = int(request.form['kor'])
    eng = int(request.form['eng'])
    math =int(request.form['math'])
    doc = {"name": name,"kor": kor,"eng": eng, "math": math}
    bitutil.stu.insertStudent(doc)
    return render_template("insertStudent.html")

@app.route("/info", methods=['POST'])
def infoStudentPost():
    irum = request.form['name']
    s = bitutil.stu.getStudent(irum)
    return render_template("infoStudent.html",s=s)


@app.route("/info/<irum>")
def infoStudent(irum):
    s = bitutil.stu.getStudent(irum)
    return render_template("infoStudent.html",s=s)


@app.route("/hello/<irum>")
def hello(irum):
   return render_template("hello.html", name=irum)


@app.route("/listStudent")
def listStudent():
    return bitutil.stu.listStudent()

@app.route("/")
def index():
    return "hello"

if __name__ == "__main__":
    app.run()
