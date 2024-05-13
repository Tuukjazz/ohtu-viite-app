CREATE TABLE article (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT UNIQUE NOT NULL,
  author TEXT NOT NULL,
  year INTEGER NOT NULL,
  journal TEXT,
  volume TEXT,
  pages TEXT,
  booktitle TEXT,
  publisher TEXT
);