from flask import Flask, render_template, request, redirect

app = Flask(__name__)
viitelista = [] # Tähän voidaan myöhemmin tallentaa viite-olioita.

@app.route("/")
def home():
    return render_template("index.html", vl=viitelista)

@app.route("/lisaaViite")
def lisaaViite():
    return render_template("lisaaViite.html", vl=viitelista)

'''
@app.route("/book")
def book():
    return render_template("book.html", vl=viitelista)

@app.route("/article")
def article():
    return render_template("article.html", vl=viitelista)

@app.route("/inproceeding")
def inproceeding():
    return render_template("inproceeding.html", vl=viitelista)

@app.route("/doi")
def doi():
    return render_template("doi.html", vl=viitelista)
'''

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
    viitelista.append({'Author': author, 'Title': title, 'Journal': journal, 'Year': year, 'Volume': volume, 'Pages': pages})
    return redirect('/')

# Tämä vaaditaan jos ohjelman ajaa: "poetry run python app.py" (Toinen vaihtoehto: "python -m flask run")
if __name__ == "__main__":
    app.run(debug=True)
