-- List the number of records with the same score of a table of a database in MySQL server
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score DESC;
