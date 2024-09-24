WITH
    leftPair AS (
        SELECT
            x,
            y,
            ROW_NUMBER() OVER(ORDER BY x ASC) as row_num
        FROM functions
    ),
    rightPair AS (
        SELECT
            x,
            y,
            ROW_NUMBER() OVER(ORDER BY x ASC) as row_num
        FROM functions
    )
SELECT
    p1.x,
    p1.y
FROM
    leftPair p1
JOIN
    rightPair p2
ON
    p1.x = p2.y AND
    p2.x = p1.y
WHERE
    p1.row_num <> p2.row_num AND
    p1.row_num < p2.row_num
ORDER BY p1.x ASC;