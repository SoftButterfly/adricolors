CREATE DATABASE adricolors;
CREATE USER adricolors WITH PASSWORD 'adricolors';
ALTER ROLE adricolors SET client_encoding TO 'utf8';
ALTER ROLE adricolors SET default_transaction_isolation TO 'read committed';
ALTER ROLE adricolors SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE adricolors TO adricolors;
