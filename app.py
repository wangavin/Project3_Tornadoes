from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

def get_db_connection():
    conn = sqlite3.connect('tornadograph.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/create/', methods=('GET', 'POST'))
def create():
    return render_template('create.html')

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM tornadoes').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)
