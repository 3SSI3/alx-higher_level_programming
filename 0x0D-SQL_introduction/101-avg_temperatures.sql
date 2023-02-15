-- Import in hbtn_0c_0 database this table
-- Displays cities average temp

SELECT city AVG(value) AS avg_temp FROM temperature GROUP BY city ORDER BY avg_temp DESC;
