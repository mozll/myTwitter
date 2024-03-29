DROP TABLE IF EXISTS users;

CREATE TABLE users(
  id                TEXT,
  username          TEXT,
  name              TEXT,
  last_name         TEXT,
  total_followers   TEXT,
  total_following   TEXT,
  total_tweets      TEXT,
  avatar            TEXT,
  cover_image       TEXT,
  PRIMARY KEY(id)
  ) WITHOUT ROWID;

INSERT INTO users VALUES("51602a9f7d82472b90ed1091248f6cb1","elonmusk","Elon", "Musk", "128900000", "177", "22700","51602a9f7d82472b90ed1091248f6cb1.jpg","coverImageELON.jpg");

INSERT INTO users VALUES("6268331d012247539998d7664bd05cc1","shakira","Shakira", "", "53700000", "235", "7999", "6268331d012247539998d7664bd05cc1.jpg","coverImageSHAKIRA.jpg");

INSERT INTO users VALUES("a22da1effb3d4f03a0f77f9aa8320203","Rihanna","Rihanna", "", "107000000", "980", "10600", "a22da1effb3d4f03a0f77f9aa8320203.jpg","coverImageRIHANNA.jpg");

INSERT INTO users VALUES("7e968791b6c24ed0a482416f0e769727","joeBiden","Joe", "Biden", "52486000", "323", "3210", "7e968791b6c24ed0a482416f0e769727.jpg", "coverImageBIDEN.jpg");

INSERT INTO users VALUES("d6389953261a48eba125fa54d8ce958e","Dupreeh","Peter", "Rasmussen", "304800", "763", "9607", "d6389953261a48eba125fa54d8ce958e.png", "coverImageDupreeh.jpg");




