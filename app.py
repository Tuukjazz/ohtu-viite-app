from doi import doiapi
from formatteri import muuttaja
from validation import validate_article
import sqlite3
from flask import Flask, render_template, request, redirect, g

DATABASE = './database.db'
app = Flask(__name__, static_folder='statics')
error_message = ""

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

@app.route("/")
def home():
    cur = get_db().cursor()
    cur.execute("select * from viite")
    viitelista = cur.fetchall()
    cur.close()
    muutettulista = muuttaja(viitelista)
    return render_template("index.html", vl=viitelista, er=error_message, ml=muutettulista)

@app.route("/submit", methods=["POST"])
def submit():
    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    journal = request.form["journal"]
    volume = request.form["volume"]
    pages = request.form["pages"]
    global error_message 
    error_message = validate_article(author, title, journal, year, volume, pages)
    if len(error_message) > 0:
        return redirect('/')
    # Tässä demotaan, että arvot on tosiaan saatu...
    print(author, title, year, journal, volume, pages, error_message)
    cur = get_db().cursor()
    cur.execute("INSERT INTO viite (author, title, year, journal, volume, pages) VALUES (?, ?, ?, ?, ?, ?)",
                (author, title, year, journal, volume, pages))
    get_db().commit()
    cur.close()
    return redirect('/')

@app.route("/delete", methods=["POST"])
def delete():
    id = request.form["id"]
    print("i: ", id)
    cur = get_db().cursor()
    cur.execute("DELETE FROM viite WHERE id = (?);", (id,))
    get_db().commit()
    cur.close()
    return redirect('/')

@app.route("/doi", methods=["POST"])
def doi():
    syote = request.form["doi"]
    doiapi(syote)
    return redirect('/')

#@app.route("/formatteri", methods=["POST"])
#def formatteri():
#    fuck you
    
# Tämä vaaditaan jos ohjelman ajaa: "poetry run python app.py" (Toinen vaihtoehto: "python -m flask run")
if __name__ == "__main__":
    app.run(debug=True)
