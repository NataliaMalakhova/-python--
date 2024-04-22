INSERT INTO Genres_list (genre_name)
VALUES
('Rock'),
('Pop'),
('Jazz');

INSERT INTO Musician (musician_name)
VALUES
('The Beatles'),
('Michael Jackson'),
('Louis Armstrong'),
('Queen');

INSERT INTO Albums_list (album_name, release_year)
VALUES
('Abbey Road', 1969),
('Thriller', 1982),
('Louis Under the Stars', 2018),
('A Night at the Opera', 1975);

INSERT INTO Track (ID_Album, track_name, duration)
VALUES
(1, 'Come Together', 260),
(2, 'My girl', 294),
(3, 'So What', 562),
(4, 'Bohemian Rhapsody', 355),
(1, 'Let It Be', 243),
(2, 'Beat It', 258);

INSERT INTO Genre (ID_Genre, ID_Musician)
VALUES
(1, 1),
(2, 2),
(3, 3),
(1, 4),
(2, 4);

INSERT INTO Album (ID_Album, ID_Musician)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4);

INSERT INTO Collections_list (collection_name, release_year)
VALUES
('Greatest Hits', 2019),
('Best of Pop', 2020),
('Jazz Legends', 1995),
('Rock Anthems', 1985);

INSERT INTO Collection (ID_Track, ID_Collection)
VALUES
(1, 1),
(4, 1),
(2, 2),
(6, 2),
(3, 3),
(1, 4),
(4, 4);
