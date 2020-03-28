-- List all shows contained in hbtn_0d_tvshows
SELECT tv_genres.name, COUNT(tv_show_genres.genre_id) AS tv_genre_count FROM tv_genres JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id GROUP BY tv_show_genres.genre_id ORDER BY tv_genre_count DESC;
