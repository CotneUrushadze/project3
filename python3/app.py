from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta
import sqlite3
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=1)

DATABASE = 'database.db'

# def db_connection():
#     conn = sqlite3.connect(DATABASE)
#     conn.row_factory = sqlite3.Row
#     return conn
#
# def add_user(username, password):
#     conn = db_connection()
#     cursor = conn.cursor()
#     query = 'INSERT INTO users (username, password) VALUES (?, ?)'
#     cursor.execute(query, (username, password))
#     conn.commit()
#     conn.close()


@app.route('/')
def tohome():
    if 'user' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        session['user'] = user
        session['password'] = password

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        query = 'INSERT INTO users (username, password) VALUES (?, ?)'
        cursor.execute(query, (user, password))
        conn.commit()
        conn.close()

        # add_user(user, password)

        return redirect(url_for('tohome'))
    # else:
    #     if 'user' in session:
    #         return redirect(url_for('tohome'))
    return render_template("login.html")

# @app.route('/home')
# def home():
#     if 'user' in session:
#         user = session['user']
#         return render_template('home.html')
#     else:
#         return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('password', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
