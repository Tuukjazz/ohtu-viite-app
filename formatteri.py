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
#     doi = {}
#   }

def muuttaja(lista, tyyppi=None):

    if tyyppi == None:
        tyyppi="bibtex"

    ml = []

    match tyyppi:

        case "bibtex":
             for viite in lista:
                pattern = r'[^a-zA-Z]'
                nimi = f'{re.split(pattern, viite[1], maxsplit=1)[0]}{viite[3]}{re.split(pattern, viite[2], maxsplit=1)[0]}'.lower()
                bibtex_entry = f"@article{{{ nimi },\n"
                bibtex_entry += f"  author = {viite[1]},\n"
                bibtex_entry += f"  title = {viite[2]},\n"
                bibtex_entry += f"  year = {viite[3]},\n"
                bibtex_entry += f"  journal = {viite[4]},\n"
                bibtex_entry += f"  volume = {viite[5]},\n"
                bibtex_entry += f"  pages = {viite[6]}\n"
                bibtex_entry += f"}}"
                ml.append(bibtex_entry)

        case "apa":
            for viite in lista:
                apa_entry = f"{{ APA Entry { viite[0] } "
                apa_entry += f"}}"
                ml.append(apa_entry)

   
    return ml
