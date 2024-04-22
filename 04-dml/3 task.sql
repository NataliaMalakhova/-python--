-- Количество исполнителей в каждом жанре
SELECT g.genre_name, COUNT(ag.ID_Musician) AS num_artists
FROM Genres_list g
LEFT JOIN Genre ag ON g.ID_genre = ag.ID_genre
GROUP BY g.genre_name;

-- Количество треков, вошедших в альбомы 2019–2020 годов
SELECT COUNT(*) AS num_tracks
FROM Track t
JOIN Albums_list a ON t.ID_album = a.ID_album
WHERE a.release_year BETWEEN 2019 AND 2020;

-- Средняя продолжительность треков по каждому альбому
SELECT a.album_name, AVG(t.duration) AS avg_duration
FROM Albums_list a
JOIN Track t ON a.ID_album = t.ID_album
GROUP BY a.album_name;

-- Все исполнители, которые не выпустили альбомы в 2020 году
SELECT musician_name
FROM Musician
WHERE ID_musician NOT IN (
    SELECT DISTINCT aa.ID_musician
    FROM Album aa
    JOIN Albums_list a ON aa.ID_album = a.ID_album
    WHERE a.release_year = 2020
);

-- Названия сборников, в которых присутствует конкретный исполнитель (допустим, выберем 'The Beatles')
SELECT c.collection_name
FROM Collections_list c
JOIN Collection ct ON c.ID_Collection = ct.ID_Collection
JOIN Track t ON ct.ID_track = t.ID_track
JOIN Albums_list a ON t.ID_album = a.ID_album
JOIN Album aa ON a.ID_album = aa.ID_album
JOIN Musician mus ON aa.ID_Musician = mus.ID_Musician
WHERE mus.musician_name = 'The Beatles';
