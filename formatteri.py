formatoitulista = [] # Tähän tallennetaan formatoitu versio viite-olioista (Esim. APA tai BibTex)

#Formatoi johonkin muotoon match casen avulla
def formatteri(formaatti):
    formatoitulista.clear()

    cur = get_db().cursor()
    cur.execute("select * from viite")
    viitelista = cur.fetchall()
    print(viitelista)
    cur.close()
    match formaatti:
        case "apa":
            for viite in viitelista:
                hlo = viite[1].split()   # Olettaa Author olevan muotoa "Etunimi Sukunimi TODO: enemmän kuin yksi
                author = hlo[0]+", "+ viite[1][0]+"."

                date = "(" + viite[3]+")" #TODO: lisättävä päivä ja kuukausi

                title = viite[2]

                journal = viite[4]

                volume = viite[5]

                pages = viite[6]

                issue = "1"  #viite['Issue']

                osoite = "https://doi.org/xxxx" #TODO: viite['Osoite'] Joko URL tai DOI

                formatoitulista.append({'Author': author, 'Date': date, 'Title': title,
                                         'Journal': journal, 'Volume': volume, 'Issue': issue, 
                                         'Pages': pages, 'Osoite': osoite})
        
        case "bibtex":
            #TODO: BibTex format
            pass
