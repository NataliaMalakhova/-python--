-- Названия альбомов, в которых присутствуют исполнители более чем одного жанра
SELECT DISTINCT a.album_name
FROM Albums_list a
JOIN Album aa ON a.id_album = aa.id_album
JOIN (
    SELECT id_musician, COUNT(DISTINCT id_genre) AS num_genres
    FROM Genre
    GROUP BY id_musician
    HAVING COUNT(DISTINCT id_genre) > 1
) ag ON aa.id_musician = ag.id_musician;

-- Наименования треков, которые не входят в сборники
SELECT track_name
FROM Track
WHERE id_track NOT IN (
    SELECT id_track
    FROM Collection
);

-- Исполнитель или исполнители, написавшие самый короткий по продолжительности трек
SELECT musician_name
FROM Musician
JOIN Album aa ON Musician.id_musician = aa.id_musician
JOIN Albums_list a ON aa.id_album = a.id_album
JOIN Track t ON a.id_album = t.id_album
WHERE t.duration = (
    SELECT MIN(duration)
    FROM Track
);

-- Названия альбомов, содержащих наименьшее количество треков
SELECT album_name
FROM Albums_list
WHERE id_album IN (
    SELECT id_album
    FROM Track
    GROUP BY id_album
    HAVING COUNT(*) = (
        SELECT MIN(track_count)
        FROM (
            SELECT COUNT(*) AS track_count
            FROM Track
            GROUP BY id_album
        ) AS min_tracks
    )
);
