from doi import doiapi
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

formatoitulista = [] # Tähän tallennetaan formatoitu versio viite-olioista (Esim. APA tai BibTex)

@app.route("/")
def home():
    cur = get_db().cursor()
    cur.execute("select * from viite")
    viitelista = cur.fetchall()
    cur.close()
    return render_template("index.html", vl=viitelista, fl=formatoitulista, er=error_message)


@app.route("/submit", methods=["POST"])
def submit():
    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    journal = request.form["journal"]
    volume = request.form["volume"]
    pages = request.form["pages"]
    error_message = validate_article(author, title, journal, year, volume, pages)
    if len(error_message) > 0:
        return redirect('/')

    # Tässä demotaan, että arvot on tosiaan saatu...
    print(author, title, year, journal, volume, pages)
    #if not is_valid(author, title, year, journal, volume, pages):
    #    return redirect('/')
    cur = get_db().cursor()
    cur.execute("INSERT INTO viite (author, title, year, journal, volume, pages) VALUES (?, ?, ?, ?, ?, ?)",
                (author, title, year, journal, volume, pages))
    get_db().commit()
    cur.close()
    formatteri("apa") #TODO: oma nappi yms
    return redirect('/')
  
@app.route("/doi", methods=["POST"])
def doi():
    syote = request.form["doi"]
    doiapi(syote)
    return redirect('/')

# Formatoi johonkin muotoon match casen avulla
def formatteri(formaatti):
    formatoitulista.clear()

    match formaatti:
        case "apa":
            for viite in viitelista:
                hlo = viite['Author'].split()   # Olettaa Author olevan muotoa "Etunimi Sukunimi TODO: enemmän kuin yksi
                author = hlo[1]+", "+ viite['Author'][0]+"."

                date = "(" + viite['Year']+")" #TODO: lisättävä päivä ja kuukausi

                title = viite['Title']

                journal = viite['Journal']

                volume = viite['Volume']

                pages = viite['Pages']

                issue = "1"  #viite['Issue']

                osoite = "https://doi.org/xxxx" #TODO: viite['Osoite'] Joko URL tai DOI

                formatoitulista.append({'Author': author, 'Date': date, 'Title': title,
                                         'Journal': journal, 'Volume': volume, 'Issue': issue, 
                                         'Pages': pages, 'Osoite': osoite})
        
        case "bibtex":
            #TODO: BibTex format
            pass


# Tämä vaaditaan jos ohjelman ajaa: "poetry run python app.py" (Toinen vaihtoehto: "python -m flask run")
if __name__ == "__main__":
    app.run(debug=True)
