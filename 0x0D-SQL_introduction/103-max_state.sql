-- Import in hbtn_0c_0 database table dump
-- Script that displays the max temp of each state, ordered by State name.

SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
