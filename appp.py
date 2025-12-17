Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from flask import Flask, render_template, request
... from datetime import date
... from data import students
... 
... app = Flask(__name__)
... 
... @app.route("/", methods=["GET", "POST"])
... def index():
...     if request.method == "POST":
...         identity = request.form["identity"]
... 
...         if identity in students:
...             name = students[identity]
...             today = date.today().strftime("%Y/%m/%d")
...             return render_template(
...                 "certificate.html",
...                 student_name=name,
...                 identity=identity,
...                 date=today
...             )
...         else:
...             return render_template(
...                 "index.html",
...                 error="الهوية غير موجودة"
...             )
... 
...     return render_template("index.html")
... 
... if __name__ == "__main__":
...     app.run()
... 
SyntaxError: multiple statements found while compiling a single statement
