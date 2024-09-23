WITH submissions_data AS (
    SELECT DISTINCT
        s.hacker_id hid,
        h.name hname,
        s.challenge_id cid,
        s.score s_score,
        MAX(score) OVER(PARTITION BY s.hacker_id, s.challenge_id) as c_max_score
    FROM
        submissions s
    JOIN
        hackers h
    ON
        h.hacker_id = s.hacker_id
)
SELECT
    hid,
    hname,
    SUM(c_max_score) as total_score
FROM
    submissions_data
WHERE
    c_max_score = s_score
GROUP BY
    hid, hname
HAVING
    SUM(c_max_score) > 0
ORDER BY
    total_score DESC, hid ASC;