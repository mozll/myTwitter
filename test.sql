DROP TABLE IF EXISTS posts;
CREATE VIRTUAL TABLE posts USING FTS5(
post_title,
post_body
);

INSERT INTO posts VALUES(
"We are trying this database","We hope this works"),
("Send a text message","We do it via fiotext"),
("Macs are great","Windows are great too");

-- SELECT * FROM posts WHERE posts MATCH "are OR message";
SELECT * FROM posts WHERE posts MATCH "are NOT trying";




DROP TABLE IF EXISTS tweets;
CREATE VIRTUAL TABLE tweets USING FTS5(
tweet_id,
tweet_message
);

INSERT INTO tweets VALUES
(1, "this is my first tweet"),
(2, "Computer games are great and so are movies"),
(3, "Counter-strike is good but what is better?");

SELECT * FROM tweets WHERE tweets MATCH 'games OR "counter-strike"';