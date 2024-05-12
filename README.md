![GHA workflow badge](https://github.com/Tuukjazz/ohtu-viite-app/actions/workflows/main.yml/badge.svg)

# ohtu-viite-app
Lähdeviiteiden tallennus nettisovellus, joka käyttää Flaskia ja SQLiteä.

### Käynnitysohje
Kotikansiossa:
```
poetry install
poetry shell
python3 app.py
```
### Käyttöohje
Lisää haluamat artikkelin tiedot ja paina lisää-nappia. Lista artikkeleista löytyy alempana.

### Debuggausta
Tietokannan debuggaus kotikansiossa:
```
sqlite3 database.db
```
Jolloin pääsee sqlite konsoliin ajamaan sql komentoja.

### Backlog
Linkki [product backlogiin](https://docs.google.com/spreadsheets/d/1Y8zzDWfnMRQlfKNQXj7rSJLi5pE2ypAosV2M5X0VCbM/edit#gid=1)

### Definition of done
Vaatimukset ovat analysoitu, suunniteltu, ohjelmoitu, testattu ja integroitu muuhun ohjelmistoon.
