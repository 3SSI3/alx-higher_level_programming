-- Lists all shows contained in database of tvshows
-- Ordered by ascending order.
-- NULL form shows without genres.

SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
        LEFT JOIN `tv_shows_genres` AS g
        ON s.`id` = g.`show_id`
ORDER BY s.`title`, g.`genre_id`;