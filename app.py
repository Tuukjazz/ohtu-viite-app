from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__, static_folder='statics')
viitelista = [] # Tähän voidaan myöhemmin tallentaa viite-olioita.

formatoitulista = [] # Tähän tallennetaan formatoitu versio viite-olioista (Esim. APA tai BibTex)

# Tarkistaa kenttien oikeellisuuden
def is_valid(author, title, journal, year, volume, pages):
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
            return False
    # Voisi lisätä virheilmoitukset

    return True

@app.route("/")
def home():
    return render_template("index.html", vl=viitelista, fl=formatoitulista)

@app.route("/submit", methods=["POST"])
def submit():
    # Tallennetaan formin kenttien sisällöt muuttujiin. Muuttujien arvoilla voidaan sitten luoda viite-olio.
    author = request.form["author"]
    title = request.form["title"]
    journal = request.form["journal"]
    year = request.form["year"]
    volume = request.form["volume"]
    pages = request.form["pages"]
    # Tässä demotaan, että arvot on tosiaan saatu...
    valid = is_valid(author, title, journal, year, volume, pages)
    if not valid:
        return render_template("index.html", vl=viitelista) #, error_message=error_message)
    viitelista.append({'Author': author, 'Title': title, 'Journal': journal, 'Year': year, 'Volume': volume, 'Pages': pages})
    formatteri("apa") #TODO: oma nappi yms
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