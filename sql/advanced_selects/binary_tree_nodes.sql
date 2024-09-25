SELECT
    n,
    CASE
        WHEN p IS NULL THEN 'Root'
        WHEN n IN (SELECT p from BST) THEN 'Inner'
        ELSE 'Leaf'
    END
FROM BST
ORDER BY n;