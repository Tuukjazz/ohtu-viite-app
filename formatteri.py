#Formatoi johonkin muotoon match casen avulla
#Esimerkki BibTex
#   @article{ id,
#     author = {},
#     title = {},
#     year = {},
#     journal = {},
#     volume = {},
#     pages = {}
#   }

def muuttaja(lista):
    ml = []
    for viite in lista:
        bibtex_entry = f"@article{{ { viite[0] },\n"
        bibtex_entry += f"  author = {viite[1]},\n"
        bibtex_entry += f"  title = {viite[2]},\n"
        bibtex_entry += f"  year = {viite[3]},\n"
        bibtex_entry += f"  journal = {viite[4]},\n"
        bibtex_entry += f"  volume = {viite[5]},\n"
        bibtex_entry += f"  pages = {viite[6]}\n"
        bibtex_entry += f"}}"
        ml.append(bibtex_entry)
    return ml
