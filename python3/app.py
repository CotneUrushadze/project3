from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta
import sqlite3


app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=10)

conn = sqlite3.connect('database.db')

def db_connection(file):
    return sqlite3.connect(file)


def add_user(user_id, username, password):
    cursor = conn.cursor()
    query = ('INSERT INTO books (title, author, price) VALUES (?, ?, ?)', (user_id, username, password))
    cursor.execute(query)




@app.context_processor
def inject_user():
    user = session.get('user')
    return dict(user=user)


@app.route('/')
def tohome():
    if 'user' in session:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        session['user'] = user
        session['password'] = password


        db_connection('database.db')
        cursor.execute('INSERT INTO users (user_id, username, password) VALUES (?, ?, ?)',
                       (1, user, password))
        conn.commit()
        return redirect(url_for('home'))




    else:
        if 'user' in session:
            return redirect(url_for('home'))
    return render_template("login.html")





@app.route('/home')
def home():
    if 'user' in session:
        user = session['user']
        return render_template('home.html')
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
