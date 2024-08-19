CREATE DATABASE remote:localhost/tfidf root oracle plocal

CREATE CLASS Document EXTENDS V
CREATE PROPERTY Document.text STRING

INSERT INTO Document (text) VALUES ('This is the first document.')
INSERT INTO Document (text) VALUES ('This document is the second document.')
INSERT INTO Document (text) VALUES ('And this is the third one.')
INSERT INTO Document (text) VALUES ('Is this the first document?')

INSERT INTO Document (text) VALUES ('The quick brown fox jumps over the lazy dog')
INSERT INTO Document (text) VALUES ('Never jump over the lazy dog quickly')
INSERT INTO Document (text) VALUES ('A lazy dog does not jump over the quick brown fox')
INSERT INTO Document (text) VALUES ('Dogs are great pets')
INSERT INTO Document (text) VALUES ('Foxes are wild animals')


