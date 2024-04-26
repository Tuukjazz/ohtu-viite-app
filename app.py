from flask import Flask, render_template, request

app = Flask(__name__)
viitelista = []

@app.route("/")
def home():
    return render_template("index.html", vl=viitelista)

@app.route("/submit", methods=["POST"])
def submit():
    testi = request.form["testi"]
    viitelista.append(testi)
    return home()

# Tämä vaaditaan jos ohjelman ajaa: "poetry run python app.py". (Toinen vaihtoehto: "python -m flask run")
if __name__ == "__main__":
    app.run(debug=True)
