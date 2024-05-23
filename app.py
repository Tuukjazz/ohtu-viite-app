from doi import doiapi
from formatteri import muuttaja
from validation import validate_article, validate_book, validate_inproceeding
import sqlite3
from flask import Flask, render_template, request, redirect, g

DATABASE = './database.db'
app = Flask(__name__, static_folder='statics')
doierror = ""
error_message = ""

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        #db.execute("""DROP TABLE viite""")
        db.execute("""CREATE TABLE IF NOT EXISTS viite(
            id INTEGER PRIMARY KEY,
            author VARCHAR(255) NOT NULL,
            title VARCHAR(255) NOT NULL,
            year INTEGER NOT NULL,
            journal VARCHAR(255),
            volume VARCHAR(50),
            pages VARCHAR(50),
            booktitle VARCHAR(255),
            publisher VARCHAR(255)
            )""")
    return db

@app.route("/")
def home():
    cur = get_db().cursor()
    cur.execute("select * from viite")
    viitelista = cur.fetchall()
    cur.close()
    muutettulista = muuttaja(viitelista)
    return render_template("index.html", vl=viitelista, er=error_message, de=doierror, ml=muutettulista)

@app.route('/haku', methods=['GET', 'POST'])
def haku():
    if request.method == 'POST':
        cur = get_db().cursor()
        hakusana = request.form['hakusana']
        hakukentta = request.form['hakutyyppi']
        tulostusmuoto = request.form['tulostusmuoto']
        cur.execute("select * from viite where " + hakukentta + " like '%" + hakusana + "%'")
        viitelista = cur.fetchall()
        cur.close()
        muutettulista = muuttaja(viitelista, tulostusmuoto)
        return render_template("index.html", vl=viitelista, de=doierror, er=error_message, ml=muutettulista)
    return render_template('index.html')

@app.route("/submit", methods=["POST", "get"])
def submit():
    value = request.form["tyyppi"]
    if value == "0":
        return redirect('/')

    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    journal = ""
    volume = ""
    pages = ""
    booktitle = ""
    publisher = ""

    if value == "1":
        journal = request.form["journal"]
        volume = request.form["volume"]
        pages = request.form["pages"]
    if value == "2":
        booktitle = request.form["booktitle"]
    if value == "3":
        publisher = request.form["publisher"]
    
    global error_message
    if value == "1":
        error_message = validate_article(author, title, year, journal, volume, pages)
        print(author, title, year, journal, volume, pages, error_message)
    if value == "2":
        error_message = validate_book(author, title, year, booktitle)
        print(author, title, year, booktitle, error_message)
    if value == "3":
        error_message = validate_inproceeding(author, title, year, publisher)
        print(author, title, year, publisher, error_message)
    
    if len(error_message) > 0:
        return redirect('/')

    # Tässä demotaan, että arvot on tosiaan saatu...
    
    cur = get_db().cursor()
    cur.execute("INSERT INTO viite (author, title, year, journal, volume, pages, booktitle, publisher) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (author, title, year, journal, volume, pages, booktitle, publisher))
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
    global doierror
    syote = request.form["doi"]
    syote = syote.strip()
    if syote == "":
        doierror = "Invalid DOI!"
    else:
        bibtex = doiapi(syote)
        if bibtex == "":
            doierror = "Invalid DOI!"
        else:
            doierror = ""
            avain = list(bibtex.keys())[0]
            try:
                author = bibtex[avain]["author"]
            except KeyError:
                author = ""
            try:
                title = bibtex[avain]["title"]
            except KeyError:
                title = ""
            try:
                year = bibtex[avain]["year"]
            except KeyError:
                year = ""
            try:
                journal = bibtex[avain]["journal"]
            except KeyError:
                journal = ""
            try:
                volume = bibtex[avain]["volume"]
            except KeyError:
                volume = ""
            try:
                pages = bibtex[avain]["pages"]
            except KeyError:
                pages = ""
            try:
                booktitle = bibtex[avain]["booktitle"]
            except KeyError:
                booktitle = ""
            try:
                publisher = bibtex[avain]["publisher"]
            except KeyError:
                publisher = ""
            cur = get_db().cursor()
            cur.execute("INSERT INTO viite (author, title, year, journal, volume, pages, booktitle, publisher) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (author, title, year, journal, volume, pages, booktitle, publisher))
            get_db().commit()
            cur.close()
    return redirect('/')

# Tämä vaaditaan jos ohjelman ajaa: "poetry run python app.py" (Toinen vaihtoehto: "python -m flask run")
if __name__ == "__main__":
    app.run(debug=True)
