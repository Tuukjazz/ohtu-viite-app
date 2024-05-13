import urllib.request
from urllib.error import HTTPError
import bibtexparser

BASE_URL = 'http://dx.doi.org/'

def doiapi(doi):
    url = BASE_URL + doi
    req = urllib.request.Request(url)
    req.add_header('Accept', 'application/x-bibtex')
    try:
        with urllib.request.urlopen(req) as f:
            bibtex = f.read().decode()
            bibtex = bibtexparser.loads(bibtex)
            bibtex_dict = bibtex.entries_dict
            # Muuntaa takaisin string-muotoon.
            # bibtex = bibtexparser.dumps(bibtex)
        return bibtex_dict
    except HTTPError as e:
        if e.code == 404:
            print('DOI not found')
        else:
            print('Service unavailable')
        return ""
