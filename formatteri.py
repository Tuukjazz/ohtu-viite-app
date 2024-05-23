import re

#Esimerkki BibTex
#   @article{ id,
#     author = {},
#     title = {},
#     year = {},
#     journal = {},
#     volume = {},
#     number = {},
#     pages = {}
#   }


#db.execute("""CREATE TABLE IF NOT EXISTS viite(
#            id INTEGER PRIMARY KEY,
#            author VARCHAR(255) NOT NULL,
#            title VARCHAR(255) NOT NULL,
#            year INTEGER NOT NULL,
#            journal VARCHAR(255),
#            volume VARCHAR(50),
#            pages VARCHAR(50),
#            booktitle VARCHAR(255),
#            publisher VARCHAR(255)
#            )""")

def muuttaja(lista, tyyppi=None):

    if tyyppi == None:
        tyyppi="bibtex"

    ml = []

    match tyyppi:

        case "bibtex":
             for viite in lista:

                if viite[7] != "" and viite[6] != "":
                    pattern = r'[^a-zA-Z]'
                    nimi = f'{re.split(pattern, viite[1], maxsplit=1)[0]}{viite[3]}{re.split(pattern, viite[2], maxsplit=1)[0]}'.lower()
                    bibtex_entry = f"@inproceedings{{{ nimi },\n"
                    bibtex_entry += f"  author = {{{viite[1]}}},\n"
                    bibtex_entry += f"  title = {{{viite[2]}}},\n"
                    bibtex_entry += f"  booktitle = {{{viite[7]}}},\n"
                    bibtex_entry += f"  year = {{{viite[3]}}},\n"
                    bibtex_entry += f"}}"
                    ml.append(bibtex_entry)

                    continue
                
                if viite[7] != "":
                    pattern = r'[^a-zA-Z]'
                    nimi = f'{re.split(pattern, viite[1], maxsplit=1)[0]}{viite[3]}{re.split(pattern, viite[2], maxsplit=1)[0]}'.lower()
                    bibtex_entry = f"@book{{{ nimi },\n"
                    bibtex_entry += f"  author = {{{viite[1]}}},\n"
                    bibtex_entry += f"  title = {{{viite[2]}}},\n"
                    bibtex_entry += f"  year = {{{viite[3]}}},\n"
                    bibtex_entry += f"  publisher = {{{viite[8]}}},\n"
                    bibtex_entry += f"}}"
                    ml.append(bibtex_entry)

                    continue

                pattern = r'[^a-zA-Z]'
                nimi = f'{re.split(pattern, viite[1], maxsplit=1)[0]}{viite[3]}{re.split(pattern, viite[2], maxsplit=1)[0]}'.lower()
                bibtex_entry = f"@article{{{ nimi },\n"
                bibtex_entry += f"  author = {{{viite[1]}}},\n"
                bibtex_entry += f"  title = {{{viite[2]}}},\n"
                bibtex_entry += f"  journal = {{{viite[4]}}},\n"
                bibtex_entry += f"  year = {{{viite[3]}}},\n"
                bibtex_entry += f"}}"
                ml.append(bibtex_entry)

        case "apa":
            ml.append("TODO")
   
    return ml
