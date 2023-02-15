-- Lists all the cities of Cali found in database hbtn_04_usa

SELECT `id`, `name`
   FROM `cities`
WHERE `state_id` IN
       (SELECT `id`
        FROM `states`
        WHERE `name` = "California")
ORDER BY `id`;