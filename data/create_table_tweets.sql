DROP TABLE IF EXISTS tweets;

CREATE TABLE tweets(
  id              TEXT,
  user_fk         TEXT,
  created_at      TEXT,
  message         TEXT,
  image           TEXT,
  updated_at      TEXT,
  total_retweets  TEXT,
  total_likes     TEXT,
  total_views     TEXT,
  total_replies   TEXT,
  PRIMARY KEY(id)
) WITHOUT ROWID;

INSERT INTO tweets VALUES(
  "1111", 
  "7e968791b6c24ed0a482416f0e769727",
  "1676283561",
  "My first tweet",
  "",
  "0",
  "0",
  "0",
  "0",
  "0"
  );

INSERT INTO tweets VALUES(
  "8", 
  "16",
  "1676283561",
  "Hello world",
  "",
  "0",
  "0",
  "0",
  "0",
  "0"
  );

