-- Creates the table force_name 
-- IF the force_name already exidsts script shouldn't fail

CREATE TABLE IF NOT EXISTS `force_name` (
    `id`   INT,
    `name` VARCHAR(256) NOT NULL
);