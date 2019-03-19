DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS agent;
DROP TABLE IF EXISTS minion;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  isadmin BOOLEAN DEFAULT False
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE agent (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'UNREGISTERED',
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  ip TEXT NOT NULL,
  port TEXT NOT NULL
);

CREATE TABLE minion(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  agent_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'unknown',
  type TEXT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (agent_id) REFERENCES agent (id)
);

INSERT INTO agent (name, status, ip, port) VALUES (1, 'local', 'RUNNING', 'x.x.x.x', 9999);
INSERT INTO minion (name, agent_id, status, type) VALUES('temperatura', 1, 'OK', 'monitor', );
INSERT INTO minion (name, agent_id, status, type) VALUES('radiador', 1, 'OK', 'actuators', );