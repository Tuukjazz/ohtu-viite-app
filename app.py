from flask import Flask, render_template, request, redirect
from doi import doiapi
from validation import validate_article

app = Flask(__name__, static_folder='statics')
viitelista = [] # Tähän voidaan myöhemmin tallentaa viite-olioita.
error_message = ""

@app.route("/")
def home():
    return render_template("index.html", vl=viitelista, em=error_message)

@app.route("/submit", methods=["POST"])
def submit():
    author = request.form["author"]
    title = request.form["title"]
    journal = request.form["journal"]
    year = request.form["year"]
    volume = request.form["volume"]
    pages = request.form["pages"]
    error_message = validate_article(author, title, journal, year, volume, pages)
    if len(error_message) > 0:
        return render_template("index.html", vl=viitelista, em=error_message)
    viitelista.append({'Author': author, 'Title': title, 'Journal': journal, 'Year': year, 'Volume': volume, 'Pages': pages})
    return redirect('/')

@app.route("/doi", methods=["POST"])
def doi():
    syote = request.form["doi"]
    doiapi(syote)
    return redirect('/')

# Tämä vaaditaan jos ohjelman ajaa: "poetry run python app.py" (Toinen vaihtoehto: "python -m flask run")
if __name__ == "__main__":
    app.run(debug=True)
