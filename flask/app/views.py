import os

from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from app import app

FILE_PATH = "E:\Programming\Python\Dodgerino-Game-Refined\highscores.db"
print(FILE_PATH)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+FILE_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(app)

class Scores(DB.Model):
    name = DB.Column(DB.String)
    score = DB.Column(DB.Integer,primary_key=True)

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Ivche'}
    return render_template('index.html',
                           user=user)

@app.route('/highscores')
def highscores():
    result = Scores.query.all() 
    return render_template('highscores.html',
                           result = result)

@app.route('/about')
def about():
    return render_template('about.html')
