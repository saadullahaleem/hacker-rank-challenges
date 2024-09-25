WITH consecutive_submissions AS (
    SELECT
        submission_date,
        hacker_id,
        ROW_NUMBER() OVER (PARTITION BY hacker_id ORDER BY submission_date) as submission_streak,
        DENSE_RANK() OVER (ORDER BY submission_date) as days_since_start
    FROM (SELECT DISTINCT submission_date, hacker_id FROM submissions) s
),
valid_streaks AS (
    SELECT
        submission_date,
        hacker_id,
        CASE WHEN submission_streak = days_since_start THEN 1 ELSE 0 END as valid_streak
    FROM consecutive_submissions
),
streaks_counts AS (
    SELECT
        submission_date,
        SUM(valid_streak) as streaks_count
    FROM valid_streaks
    GROUP BY submission_date
),
hacker_submissions_count AS (
    SELECT
        s.submission_date,
        s.hacker_id,
        COUNT(DISTINCT submission_id) as submissions_count,
        ROW_NUMBER() OVER(
            PARTITION BY s.submission_date
            ORDER BY COUNT(DISTINCT submission_id) DESC, s.hacker_id ASC
        ) as ranking
    FROM submissions s
    GROUP BY s.submission_date, s.hacker_id
    ORDER BY submission_date DESC
)
SELECT
    hsc.submission_date,
    sc.streaks_count,
    hsc.hacker_id,
    h.name
FROM hacker_submissions_count hsc
JOIN hackers h ON hsc.hacker_id = h.hacker_id
JOIN streaks_counts sc ON sc.submission_date = hsc.submission_date
WHERE hsc.ranking = 1
ORDER BY hsc.submission_date;