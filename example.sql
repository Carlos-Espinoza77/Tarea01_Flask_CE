#son comandos de SQL que se ejecutan uno a la vez

DROP TABLE IF EXISTS post;

CREATE TABLE post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

INSERT INTO post (title, content) VALUES ('Primer post', 'Que tal pythonistas');
INSERT INTO post (title, content) VALUES ('Segundo post', 'Buen día con todos');

.headers on
.mode column