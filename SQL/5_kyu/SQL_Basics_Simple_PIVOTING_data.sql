-- For this challenge you need to PIVOT data. You have two tables, products and 
-- details. Your task is to pivot the rows in products to produce a table of 
-- products which have rows of their detail. Group and Order by the name of 
-- the Product.

-- Tables and relationship below:


-- You must use the CROSSTAB statement to create a table that has the schema 
-- as below:

-- CROSSTAB table.

-- name
-- good
-- ok
-- bad
-- Compare your table to the expected table to view the expected results.


CREATE EXTENSION tablefunc;

SELECT *
FROM 
CROSSTAB( 
    'SELECT p.name, d.detail, COUNT(d.detail)::INT
    FROM products p
    JOIN details d
    ON p.id = d.product_id
    GROUP BY p.name, d.detail
    ORDER BY p.name,
            CASE WHEN d.detail=''good'' THEN COUNT(d.detail)::INT END,
            CASE WHEN d.detail=''ok'' THEN COUNT(d.detail)::INT END,
            CASE WHEN d.detail=''bad'' THEN COUNT(d.detail)::INT END'
        )
  AS ct (name text, good int, ok int, bad int);
