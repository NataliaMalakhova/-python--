-- Название и продолжительность самого длительного трека.
SELECT track_name, duration FROM Track WHERE duration = (SELECT MAX(duration) FROM Track);

-- Название треков, продолжительность которых не менее 3,5 минут.
SELECT track_name FROM Track WHERE duration >= 210; -- 3.5 минуты * 60 секунд = 210 секунд

-- Названия сборников, вышедших в период с 2018 по 2020 год включительно.
SELECT collection_name FROM collections_list WHERE release_year BETWEEN 2018 AND 2020;

-- Исполнители, чьё имя состоит из одного слова.
SELECT musician_name FROM Musician WHERE musician_name NOT LIKE '% %'; -- Нет пробелов в имени

-- Название треков, которые содержат слово «мой» или «my».
SELECT track_name FROM Track WHERE track_name ILIKE '%мой%' OR track_name ILIKE '%my%';

