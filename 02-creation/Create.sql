CREATE TABLE Musician
(
    ID_Musician SERIAL PRIMARY KEY,
    musician_name CHARACTER VARYING(50)
);

CREATE TABLE Genres_list
(
    ID_Genre SERIAL PRIMARY KEY,
    genre_name CHARACTER VARYING(30)
);

CREATE TABLE Genre
(
    ID_Musician_Genre SERIAL PRIMARY KEY,
    ID_Genre INTEGER,
    ID_Musician INTEGER,
    FOREIGN KEY (ID_Genre) REFERENCES Genres_list (ID_Genre),
    FOREIGN KEY (ID_Musician) REFERENCES Musician (ID_Musician)
);

CREATE TABLE Albums_list
(
    ID_Album SERIAL PRIMARY KEY,
    album_name CHARACTER VARYING(50),
  	release_year INTEGER
);

CREATE TABLE Album
(
    ID_Musician_Album SERIAL PRIMARY KEY,
    ID_Album INTEGER,
    ID_Musician INTEGER,
    FOREIGN KEY (ID_Album) REFERENCES Albums_list (ID_Album),
    FOREIGN KEY (ID_Musician) REFERENCES Musician (ID_Musician)
);

CREATE TABLE Track
(
    ID_Track SERIAL PRIMARY KEY,
    ID_Album INTEGER,
    track_name CHARACTER VARYING(50),
  	duration INTEGER,
    FOREIGN KEY (ID_Album) REFERENCES Albums_list (ID_Album)
);

CREATE TABLE Collections_list
(
    ID_Collection SERIAL PRIMARY KEY,
    collection_name CHARACTER VARYING(50),
  	release_year INTEGER
);

CREATE TABLE Collection
(
    ID_Track_Collection SERIAL PRIMARY KEY,
    ID_Track INTEGER,
    ID_Collection INTEGER,
    FOREIGN KEY (ID_Track) REFERENCES Track (ID_Track),
    FOREIGN KEY (ID_Collection) REFERENCES Collections_list (ID_Collection)
);
