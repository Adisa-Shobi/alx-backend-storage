-- a SQL script that lists all bands with Glam rock as their
-- main style, ranked by their longevity
-- CREATE PROCEDURE calc_lifespan (IN formed INT, IN brokeup INT, OUT lifespan INT)
-- BEGIN DECALRE year INT SET year = 2023 IF BROKEUP THEN SET lifespan =
-- brokeup - formed ELSE SET lifes--pan = year - formed END IF END;
SELECT band_name, COALESCE(split, 2023) - formed AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%';
