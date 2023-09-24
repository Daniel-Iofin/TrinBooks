from flask import Flask
from flask import request
from flask import render_template
import sqlite3
from random import randint
app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def index():
    bookDB = sqlite3.connect("bookDB.db")
    cursor = bookDB.cursor()
    cursor.execute("SELECT * FROM listings;")

    data = cursor.fetchall()
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/new-listing', methods=['GET', 'POST'])
def newListing():
    if request.method == 'POST':
        email = request.form['email']
        title = request.form['title']
        course = request.form['course']
        condition = request.form['condition']
        price = request.form['price']
        info = request.form['info']

        with sqlite3.connect("bookDB.db") as bookDB:
            cursor = bookDB.cursor()
            cursor.execute("INSERT INTO listings values(?, ?, ?, ?, ?, ?, ?);", (randint(0, 9223372036854775807), email, title, course, condition, price, info))
            bookDB.commit()
        
    return render_template('new-listing.html')

app.run(debug=True)
