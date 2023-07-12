CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE profile (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dob VARCHAR(100) NOT NULL,
    user_id  INTEGER UNIQUE,
    FOREIGN KEY (user_id) REFERENCES "user" (id)
);

CREATE TABLE accounts (
    id SERIAL PRIMARY KEY, 
    server_id VARCHAR(255) UNIQUE NOT NULL,
    user_id INTEGER UNIQUE,
    FOREIGN KEY (user_id) REFERENCES "user" (id)

);

CREATE TABLE web_server (
    id SERIAL PRIMARY KEY,
    server_id VARCHAR(255) UNIQUE NOT NULL,
    server_ip VARCHAR(100) UNIQUE NOT NULL,
    server_name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE data (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    email VARCHAR(255),
    password VARCHAR(100),
    preferences VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES "user" (id)
);

ALTER TABLE accounts
ADD FOREIGN KEY (server_id) 
REFERENCES web_server (server_id);


