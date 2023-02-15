-- List all comedy shows in database hbtn_0d_tv_shows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Results must be sorted in ascending order by the show title.

SELECT t.`title`
  FROM `tv_shows` AS t
       INNER JOIN `tv_show_genres` AS s
       ON t.`id` = s.`show_id`

       INNER JOIN `tv_genres` AS g
       ON g.`id` = s.`genre_id`
       WHERE g.`name` = "Comedy"
 ORDER BY t.`title`;