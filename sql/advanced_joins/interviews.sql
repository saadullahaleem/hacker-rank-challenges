WITH
    ss AS (
        SELECT
            ch.challenge_id,
            ch.college_id,
            COALESCE(SUM(s.total_submissions), 0) as ts,
            COALESCE(SUM(s.total_accepted_submissions), 0) as tas
        FROM
            Challenges ch
        LEFT JOIN
            submission_stats s ON s.challenge_id = ch.challenge_id
        GROUP BY ch.challenge_id, ch.college_id
    ),
    vs AS (
        SELECT
            ch.challenge_id,
            ch.college_id,
            COALESCE(SUM(vs.total_views), 0) as tv,
            COALESCE(SUM(vs.total_unique_views), 0) as tuv
        FROM
            Challenges ch
        LEFT JOIN
            view_stats vs ON vs.challenge_id = ch.challenge_id
        GROUP BY ch.challenge_id, ch.college_id
    )

SELECT
    c.contest_id,
    c.hacker_id,
    c.name,
    SUM(ss.ts),
    SUM(ss.tas),
    SUM(vs.tv),
    SUM(vs.tuv)
FROM contests c
JOIN colleges cs ON cs.contest_id = c.contest_id
JOIN challenges ch ON ch.college_id = cs.college_id
JOIN vs ON vs.challenge_id = ch.challenge_id
JOIN ss ON ss.challenge_id = ch.challenge_id
GROUP BY c.contest_id, c.hacker_id, c.name
HAVING SUM(ss.ts) + SUM(ss.tas) + SUM(vs.tv) + SUM(vs.tuv) > 0
ORDER BY c.contest_id;