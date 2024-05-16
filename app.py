from doi import doiapi
from formatteri import muuttaja
from validation import validate_article
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
        cur.execute("select * from viite where " + hakukentta + " like '%" + hakusana + "%'")
        viitelista = cur.fetchall()
        cur.close()
        muutettulista = muuttaja(viitelista)
        return render_template("index.html", vl=viitelista, de=doierror, er=error_message, ml=muutettulista)
    return render_template('index.html')

@app.route("/submit", methods=["POST"])
def submit():
    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    try: 
        journal = request.form["journal"]
    except:
        journal = ""
    try: 
        volume = request.form["volume"]
    except:
        volume = ""
    try: 
        pages = request.form["pages"]
    except:
        pages = ""
    try: 
        booktitle = request.form["booktitle"]
    except:
        booktitle = ""
    try: 
        publisher = request.form["publisher"]
    except:
        publisher = ""

    global error_message 
    error_message = validate_article(author, title, journal, year, volume, pages, booktitle, publisher)
    if len(error_message) > 0:
        return redirect('/')
    # Tässä demotaan, että arvot on tosiaan saatu...
    print(author, title, year, journal, volume, pages, error_message)
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
    bibtex = doiapi(syote)
    if bibtex == "":
        doierror = "Virheellinen DOI!"
    else:
        doierror = ""
        avain = list(bibtex.keys())[0]
        cur = get_db().cursor()
        cur.execute("INSERT INTO viite (author, title, year, journal, volume, pages) VALUES (?, ?, ?, ?, ?, ?)",
                    (bibtex[avain]["author"], bibtex[avain]["title"], bibtex[avain]["year"], bibtex[avain]["journal"], bibtex[avain]["volume"], bibtex[avain]["pages"]))
        get_db().commit()
        cur.close()
    return redirect('/')

# Tämä vaaditaan jos ohjelman ajaa: "poetry run python app.py" (Toinen vaihtoehto: "python -m flask run")
if __name__ == "__main__":
    app.run(debug=True)
