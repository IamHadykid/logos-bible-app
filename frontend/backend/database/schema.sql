-- Bible Books Table
CREATE TABLE bible_books (
  id INTEGER PRIMARY KEY,
  name TEXT,
  testament TEXT
);

-- Bible Verses Table
CREATE TABLE bible_verses (
  id INTEGER PRIMARY KEY,
  book TEXT,
  chapter INTEGER,
  verse INTEGER,
  text TEXT,
  translation TEXT
);

-- Hebrew & Greek Lexicon
CREATE TABLE lexicon (
  strongs TEXT PRIMARY KEY,
  original_word TEXT,
  transliteration TEXT,
  meaning TEXT,
  language TEXT
);
