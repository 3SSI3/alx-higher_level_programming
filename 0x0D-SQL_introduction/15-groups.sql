-- lists all the number of records with same score,
-- result should display; score & no of records (number)
-- sorted desceding order

SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
