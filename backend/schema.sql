DROP TABLE IF EXISTS posts;

CREATE TABLE twitter (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    batch INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    conversation_id INTEGER ,
    date_created DATETIME ,
    username VARCHAR(255) ,
    name VARCHAR(255) ,
    place VARCHAR(255) ,
    tweet VARCHAR(1500) ,
    language VARCHAR(255) ,
    mentions VARCHAR(255) ,
    urls VARCHAR(255) ,
    photos VARCHAR(255) ,
    replies_count INTEGER ,
    retweets_count INTEGER ,
    likes_count INTEGER ,
    hashtags VARCHAR(255) ,
    link VARCHAR(255) ,
    thumbnail VARCHAR(255)
);
