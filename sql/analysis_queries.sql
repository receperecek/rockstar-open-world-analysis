-- Baseline metadata
SELECT game_id, title, release_year, platforms FROM game_metadata ORDER BY release_year;

    -- Catalogue rows by game; this is not a verified main-story mission total.
SELECT game_id, COUNT(*) AS catalogue_rows
FROM mission_catalogue
GROUP BY game_id;

-- Primary mechanical distribution
SELECT primary_mechanic, COUNT(*) AS missions
FROM mission_catalogue
GROUP BY primary_mechanic
ORDER BY missions DESC;

-- Optional activity comparison
SELECT game_id, activity_type, activity_count
FROM optional_missions_activities
ORDER BY game_id, activity_count DESC;
