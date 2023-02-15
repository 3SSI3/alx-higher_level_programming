-- List all records with conditions;
-- Don't list rows without a name value
-- result shoud display the score & name (in this order)
-- descending order

SELECT score, name FROM second_table WHERE name  IS NOT NULL ORDER BY score DESC;
