import re

# Tarkistaa kenttien oikeellisuuden
def validate_article(author, title, journal, year, volume, pages):
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
    error_messages = {
        'author': 'Author field cannot be empty.',
        'title': 'Title field cannot be empty.',
        'journal': 'Journal field cannot be empty.',
        'year': 'Year must be a four-digit number (YYYY).',
        'volume': 'Volume must be a positive integer.',
        'pages': 'Pages must be a range in the format "start-end" or a single number.'
    }
    # returns only first error, needs change so every error is returned
    for field, field_value in fields.items():
        value = re.compile(field_syntax[field])
        if not value.fullmatch(field_value):
            return error_messages[field]

    return ""
def validate_book(author, title, year, booktitle):
    fields = {
        'author': author,
        'title': title,
        'year': year,
        'booktitle': booktitle
    }
    field_syntax = {
        'author': '.+',
        'title': '.+',
        'year': '[0-9]{4}',
        'booktitle': '.+',
    }
    error_messages = {
        'author': 'Author field cannot be empty.',
        'title': 'Title field cannot be empty.',
        'year': 'Year must be a four-digit number (YYYY).',
        'booktitle': 'Booktitle field cannot be empty'
    }
    # returns only first error, needs change so every error is returned
    for field, field_value in fields.items():
        value = re.compile(field_syntax[field])
        if not value.fullmatch(field_value):
            return error_messages[field]

    return ""
def validate_inproceeding(author, title, year, publisher):
    fields = {
        'author': author,
        'title': title,
        'year': year,
        'publisher': publisher

    }
    field_syntax = {
        'author': '.+',
        'title': '.+',
        'year': '[0-9]{4}',
        'publisher': '.+'
    }
    error_messages = {
        'author': 'Author field cannot be empty.',
        'title': 'Title field cannot be empty.',
        'year': 'Year must be a four-digit number (YYYY).',
        'publisher': 'Publisher field cannot be empty'
    }
    # returns only first error, needs change so every error is returned
    for field, field_value in fields.items():
        value = re.compile(field_syntax[field])
        if not value.fullmatch(field_value):
            return error_messages[field]

    return ""