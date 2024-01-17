-- sr5t ywr yhw4 t
-- qa5 eyq45y eqy4
SELECT
tv_show_genres.genre_id AS genre,
COUNT(tv_shows.id) AS number_of_shows
FROM
tv_show_genres
JOIN
tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY
tv_show_genres.genre_id
ORDER BY
number_of_shows DESC;
