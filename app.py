from flask import Flask, app, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://shalin:Chepkoech03@localhost/students'

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    id=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(40))
    lname=db.Column(db.String(40))
    pet=db.Column(db.String(40))

    def __init__(self,fname,lname,pet):
        self.fname=fname
        self.lname=lname
        self.pet=pet

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)