import sqlite3
from flask import Flask, render_template, request, redirect, g
import re

DATABASE = './database.db'
app = Flask(__name__, static_folder='statics')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.execute("""CREATE TABLE IF NOT EXISTS viite(
            id INTEGER PRIMARY KEY,
            author VARCHAR(255) NOT NULL,
            title VARCHAR(255) NOT NULL,
            year INTEGER NOT NULL,
            journal VARCHAR(255) NOT NULL,
            volume VARCHAR(50) NOT NULL,
            pages VARCHAR(50) NOT NULL
            )""")
    return db



# Tarkistaa kenttien oikeellisuuden
def is_valid(author, title, year, journal, volume, pages):
    fields = {
        'author': author,
        'title': title,
        'journal': journal,
        'year': year,
        'volume': volume,
        'pages': pages
    }
    field_syntax = {
        'author': '.+',
        'title': '.+',
        'journal': '.+',
        'year': '[0-9]{4}',
        'volume': '[0-9]+',
        'pages': '[0-9]+(-[0-9]+)?'
    }
    
    for field, field_value in fields.items():
        value = re.fullmatch(field_syntax[field], field_value)
        if not value:
            print(field, value)
            return False
    # Voisi lisätä virheilmoitukset
    return True

@app.route("/")
def home():
    cur = get_db().cursor()
    cur.execute("select * from viite")
    viitelista = cur.fetchall()
    cur.close()
    return render_template("index.html", vl=viitelista)

@app.route("/submit", methods=["POST"])
def submit():
    # Tallennetaan formin kenttien sisällöt muuttujiin. Muuttujien arvoilla voidaan sitten luoda viite-olio.
    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    journal = request.form["journal"]
    volume = request.form["volume"]
    pages = request.form["pages"]
    # Tässä demotaan, että arvot on tosiaan saatu...
    print(author, title, year, journal, volume, pages)
    if not is_valid(author, title, year, journal, volume, pages):
        return redirect('/')
    cur = get_db().cursor()
    cur.execute("INSERT INTO viite (author, title, year, journal, volume, pages) VALUES (?, ?, ?, ?, ?, ?)",
                (author, title, year, journal, volume, pages))
    get_db().commit()
    cur.close()
    return redirect('/')

# Tämä vaaditaan jos ohjelman ajaa: "poetry run python app.py" (Toinen vaihtoehto: "python -m flask run")
if __name__ == "__main__":
    app.run(debug=True)
