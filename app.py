from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)
viitelista = [] # Tähän voidaan myöhemmin tallentaa viite-olioita.

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
    return render_template("index.html", vl=viitelista)

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
    return redirect('/')

# Tämä vaaditaan jos ohjelman ajaa: "poetry run python app.py" (Toinen vaihtoehto: "python -m flask run")
if __name__ == "__main__":
    app.run(debug=True)