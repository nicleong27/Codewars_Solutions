-- This kata is inspired by SQL Basics: Simple PIVOTING data by matt c.

-- You need to build a pivot table WITHOUT using CROSSTAB function. Having 
-- two tables products and details you need to select a pivot table of products 
-- with counts of details occurrences (possible details values are ['good', 
-- 'ok', 'bad'].

-- Results should be ordered by product's name.

-- Model schema for the kata is:

-- schema

-- your query should return table with next columns

-- name
-- good
-- ok
-- bad
-- Compare your table to the expected table to view the expected results.


SELECT p.name, 
      SUM(CASE WHEN d.detail = 'good' THEN 1 ELSE 0 END) AS good,
      SUM(CASE WHEN d.detail = 'ok' THEN 1 ELSE 0 END) AS ok,
      SUM(CASE WHEN d.detail = 'bad' THEN 1 ELSE 0 END) AS bad
FROM products p 
JOIN details d
ON p.id = d.product_id
GROUP BY p.name
ORDER BY p.nam