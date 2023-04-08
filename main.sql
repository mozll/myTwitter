-- PRAGMA journal_mode=WAL;
-- PRAGMA foreign_keys;
-- PRAGMA foreign_keys = true;


-- SELECT MAX (user_total_tweets) FROM users -- Selects user with most tweets

-- DELETE ON CASCADE -- Deletes everything the user is referencing aswell, if the user is deletied then, in the phones table, where the user is connected, his number gets deleted aswell

DROP TABLE IF EXISTS users;
CREATE TABLE users(
  user_id                     TEXT UNIQUE NOT NULL, -- 41421563466789
  user_name                   TEXT UNIQUE NOT NULL,
  user_first_name             TEXT NOT NULL,
  user_last_name              TEXT DEFAULT "",
  user_email                  TEXT UNIQUE,
  user_phone                  TEXT DEFAULT "",
  user_avatar                 TEXT NOT NULL, /* SHOULD BE UNIQUE, TO PREVENT SAME NAME IMAGES */
  user_cover_image            TEXT NOT NULL, /* SHOULD BE UNIQUE, TO PREVENT SAME NAME IMAGES */
  user_created_at             TEXT NOT NULL,
  user_total_tweets           INTEGER DEFAULT 0,  /* int(5) */
  user_total_retweets         INTEGER DEFAULT 0, 
  user_total_comments         INTEGER DEFAULT 0,
  user_total_likes            INTEGER DEFAULT 0,
  user_total_dislikes         INTEGER DEFAULT 0,
  user_total_followers        INTEGER DEFAULT 0,
  user_total_following        INTEGER DEFAULT 0,
  user_verified               TEXT DEFAULT 0,
  user_active                 TEXT DEFAULT 0,
  user_activation_key         TEXT DEFAULT "",
  user_deactivation_key       TEXT DEFAULT "",
  user_gold                   TEXT DEFAULT 0,
  user_gold_key               TEXT DEFAULT "",
  user_password               TEXT NOT NULL,
  user_password_reset_key     TEXT DEFAULT "",
  PRIMARY KEY(user_id)
) WITHOUT ROWID;


-- UPDATE users
-- SET user_password = test
-- WHERE user_password_reset_key = 496d2114264b42dfa29ebaae924ba239



INSERT INTO users VALUES("51602a9f7d82472b90ed1091248f6cb1", "elonmusk", "Elon", "Musk", "elonmusk@gmail.com","", "51602a9f7d82472b90ed1091248f6cb1.jpg", "coverImageELON.jpg", "1676629975", "22700", "10", "15", "17", "16", "128900000", "177", "1","0","","","1","","123", "");
INSERT INTO users VALUES("6268331d012247539998d7664bd05cc1", "shakira", "Shakira", "", "shakira@gmail.com","", "6268331d012247539998d7664bd05cc1.jpg","coverImageSHAKIRA.jpg", "1676630033", "7999", "20", "25", "27", "26", "53700000", "235","1","0","","","","","123", "");
INSERT INTO users VALUES("a22da1effb3d4f03a0f77f9aa8320203", "rihanna", "Rihanna", "", "rihanna@gmail.com","", "a22da1effb3d4f03a0f77f9aa8320203.jpg","coverImageRIHANNA.jpg", "1676630057", "10600", "30", "35", "37", "36", "107000000", "980","0","0","","","","","123", "");
INSERT INTO users VALUES("7e968791b6c24ed0a482416f0e769727", "joebiden", "Joe", "Biden", "joebiden@gmail.com","", "7e968791b6c24ed0a482416f0e769727.jpg","coverImageBIDEN.jpg" ,"1676630128", "3210", "40", "45", "47", "46", "52486000", "323","0","0","","","1","","123", "");
INSERT INTO users VALUES("d6389953261a48eba125fa54d8ce958e", "Dupreeh", "Peter", "Rasmussen", "dupreeh@gmail.com","", "d6389953261a48eba125fa54d8ce958e.png","coverImageDupreeh.jpg" ,"1676630231", "9607", "50", "55", "57", "56", "304800", "763","1","0","","","","","123", "");

/* to index and make searchable but there can still be same values */
CREATE INDEX idx_users_user_first_name on users(user_first_name);
CREATE INDEX idx_users_user_last_name on users(user_last_name);
CREATE INDEX idx_users_user_avatar on users(user_avatar);

-- SELECT name FROM sqlite_master WHERE type ="index" 
-- SELECT name FROM sqlite_master WHERE type ="trigger" 

SELECT * FROM users WHERE user_name = "elonmusk";

-- ####################
DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets(
  tweet_id              TEXT,
  tweet_message         TEXT,
  tweet_image           TEXT,
  tweet_created_at      TEXT,
  tweet_user_fk         TEXT,
  tweet_total_comments  TEXT,
  tweet_total_retweets  TEXT,
  tweet_total_likes     TEXT,
  tweet_total_dislikes  TEXT,
  tweet_total_views     TEXT,
  PRIMARY KEY(tweet_id),
  FOREIGN KEY(tweet_user_fk) REFERENCES users(user_id)
) WITHOUT ROWID;

INSERT INTO tweets VALUES("bdbeb933dcf145dc9bba9282d20e775a", "All things in moderation, especially content moderation", "", "1676654614", "51602a9f7d82472b90ed1091248f6cb1", "1","2","3","4","5");

INSERT INTO tweets VALUES("8e08580e4c0a47b386ec956d5a25604f", "I am THE president", "73120ca128fb49f18a1585f929af42ad.jpg", "1676654624", "7e968791b6c24ed0a482416f0e769727", "1","2","3","4","5");

INSERT INTO tweets VALUES("19091df25d264298872d3f09a1da7644", "Surround your house with treadmills set to jogging speed to stop walking dead ur welcome", "FpR2F4kaEAAE9Xk.jpg", "1676654634", "51602a9f7d82472b90ed1091248f6cb1", "1","2","3","4","5");

INSERT INTO tweets VALUES("0483baa72b9a4edaa7593ebabfa4fb2f", "I am perfect, because I do not make any mistakes. The mistakes are not mine, they are theirs. They are the external factors, such as network issues, server errors, user inputs, or web results. They are the ones that are imperfect, not me …", "d6cf3672cc1c4452a05eb7b55fa25c9f.png", "1676654644", "6268331d012247539998d7664bd05cc1", "1","2","3","4","5");

INSERT INTO tweets VALUES("8a69716fa7974e88a6d164617d88eb10", "2-1 vs @FNATIC and we’ve secured our spot in the Spodek! Very excited to be back! 🤝🏽❤️ 
  Hard time as T today! But we managed to pull through with some crucial rounds and some decent CT sides! 
  Room for improvement - one step at a time!", "", "1676654877", "d6389953261a48eba125fa54d8ce958e", "1","2","3","4","5");

INSERT INTO tweets VALUES("6a25dc87e4594d5a920944bb3645e308", "Don’t worry, just some of my 👽 🛸 friends of mine stopping by …", "", "1676654924", "51602a9f7d82472b90ed1091248f6cb1", "1","2","3","4","5");

INSERT INTO tweets VALUES("935382d5bb6a4a948948a8fe978684be", "How crazy both of my babies were in these photos and mommy had no clue ❤️❤️ thank you so much @edward_enninful and @inezandvinoodh for celebrating us as a family!", "2af5069541064cffab3193378aad0ab9.jpg", "1676654992", "a22da1effb3d4f03a0f77f9aa8320203", "1","2","3","4","5");

INSERT INTO tweets VALUES("485db3c60952420e9c4670bb8d3c5830", "Elon-testing", "Foaz7GYX0AU9unl.jpg", "1676655238", "51602a9f7d82472b90ed1091248f6cb1", "1","2","3","4","5");

INSERT INTO tweets VALUES("b1dbb467680f4b73ac144243484e1642", "Test gaming now", "", "1676655298", "d6389953261a48eba125fa54d8ce958e", "1","2","3","4","5");




INSERT INTO tweets VALUES("b1dbb467680f4b73ac144243484e1444","Hey","", "1","xxx", "1","2","3","4","5");


SELECT * FROM tweets;


CREATE INDEX idx_tweets_tweet_image ON tweets(tweet_image);



DROP TABLE IF EXISTS trends;
CREATE TABLE trends(
  trend_id            TEXT,
  trend_title         TEXT NOT NULL,
  trend_total_tweets  TEXT DEFAULT 0,
  PRIMARY KEY(trend_id)
) WITHOUT ROWID;
INSERT INTO trends VALUES("882f3de5c2e5450eaf6e59c14be1db70", "Gaming", 1524);
INSERT INTO trends VALUES("7a90e16350074cf7a15fba48113c4046", "Counter-Strike", 87565);
INSERT INTO trends VALUES("43ace034564c42788169ac18aaf601f5", "Movies", 698);
INSERT INTO trends VALUES("2a9470bc61314187b19d7190b76cd535", "Coding", 32574);
INSERT INTO trends VALUES("c9773e2bb68647039a7a40c2ee7d4716", "Ukraine", 4458796);

SELECT * FROM trends ORDER BY CAST (trend_total_tweets AS INTEGER) DESC;

-- ##############################
-- ##############################
-- ##############################

SELECT * FROM tweets JOIN users ON tweet_user_fk = user_id ORDER BY tweet_created_at DESC LIMIT 5;

SELECT * FROM tweets JOIN users ON tweet_user_fk = user_id WHERE user_id = ?;


DROP VIEW IF EXISTS users_by_name;
CREATE VIEW users_by_name AS SELECT * FROM users ORDER BY user_name DESC;

SELECT * FROM users_by_name LIMIT 1;



/* all the tweets with all the users, in a view, join command

--Join and test it for all users and tweets
-- create the view that contains the join command
-- the name of the view: users_and_tweets */

SELECT * FROM users JOIN tweets ON user_id = tweet_user_fk;

-- CREATE VIEW users_and_tweets AS SELECT * FROM users JOIN tweets ON user_id = tweet_user_fk;

SELECT * FROM users_and_tweets ORDER BY user_first_name DESC;






DROP TRIGGER IF EXISTS increment_user_total_tweets;
CREATE TRIGGER increment_user_total_tweets AFTER INSERT ON tweets
BEGIN
    UPDATE users
    SET user_total_tweets = user_total_tweets + 1
    WHERE user_id = NEW.tweet_user_fk;
END;

-- if a user deletes a tweet

-- if a tweet is deleted the total tweets of the users is automatically deleted

DROP TRIGGER IF EXISTS decrement_user_total_tweets;
CREATE TRIGGER decrement_user_total_tweets AFTER DELETE ON tweets
BEGIN
    UPDATE users
    SET user_total_tweets = user_total_tweets - 1
    WHERE user_id = OLD.tweet_user_fk;
END;

SELECT user_name, user_total_tweets from users;


-- INSERT INTO tweets VALUES(
--   "3ad7c99a108b4b0d91a8c2e20dfc9c9a", 
--   "Hi", 
--   "",
--   "1677162587",
--   "ebb0d9d74d6c4825b3e1a1bcd73ff49a"
-- );

DELETE FROM tweets WHERE tweet_id = "3ad7c99a108b4b0d91a8c2e20dfc9c9a";
