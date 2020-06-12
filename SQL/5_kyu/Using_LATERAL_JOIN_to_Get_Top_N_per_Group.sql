-- Given the schema presented below write a query, which uses a LATERAL join, 
-- that returns two most viewed posts for every category.

-- Order the result set by:

-- category name alphabetically
-- number of post views largest to lowest
-- post id lowest to largest
-- Note:

-- Some categories may have less than two or no posts at all.
-- Two or more posts within the category can be tied by (have the same) the 
-- number of views. Use post id as a tie breaker - a post with a lower id gets 
-- a higher rank.

-- Schema

-- categories

--  Column     | Type                        | Modifiers
-- ------------+-----------------------------+----------
-- id          | integer                     | not null
-- category    | character varying(255)      | not null
-- posts

--  Column     | Type                        | Modifiers
-- ------------+-----------------------------+----------
-- id          | integer                     | not null
-- category_id | integer                     | not null
-- title       | character varying(255)      | not null
-- views       | integer                     | not null
-- Desired Output

-- The desired output should look like this:

-- category_id | category | title                             | views | post_id
-- ------------+----------+-----------------------------------+-------+--------
-- 5           | art      | Most viewed post about Art        | 9234  | 234
-- 5           | art      | Second most viewed post about Art | 9234  | 712
-- 2           | business | NULL                              | NULL  | NULL
-- 7           | sport    | Most viewed post about Sport      | 10    | 126
-- ...
-- category_id - category id
-- category - category name
-- title - post title
-- views - the number of post views
-- post_id - post id

SELECT c.id AS category_id, 
        c.category, 
        sub1.title, 
        sub1.views, 
        sub1.id AS post_id
FROM categories c
LEFT JOIN LATERAL (
        SELECT category_id, id, title, SUM(views) AS views
        FROM posts 
        WHERE c.id = category_id
        GROUP BY category_id, id, title
        ORDER BY SUM(views) DESC, id
        LIMIT 2
        ) sub1 ON TRUE
ORDER BY c.category, sub1.views DESC, post_id