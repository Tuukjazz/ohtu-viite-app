class Ref(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(2000), unique=False, nullable=False)
    year = db.Colums(db.String(4), unique=False, nullable=False)
    journal = db.Columns(db.String(250), unique=False, nullable=False)
    volume = db.Columns(db.String(50), unique=False, nullable=False)
    pages = db.Columns(db.String(50), unique=False, nullable=False)
    booktitle = db.Columns(db.String(250), unique=False, nullable=False)
    publisher = db.Columns(db.String(250), unique=False, nullable=False)



    def __repr__(self):
        return f"Ref('{self.title}', '{self.author}', '{self.year}')"

