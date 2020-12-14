CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    text TEXT,
    post_time DATETIME DEFAULT CURRENT_TIMESTAMP
);