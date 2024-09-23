WITH challenges_data AS
(
    SELECT
        h.hacker_id as hid,
        h.name as hname,
        COUNT(c.challenge_id) as c_count,
        MAX(COUNT(c.challenge_id)) OVER() as mc_count,
        COUNT(h.hacker_id) OVER(PARTITION BY COUNT(c.challenge_id)) AS gc_count
    FROM hackers h
    JOIN challenges c on c.hacker_id = h.hacker_id
    GROUP BY h.hacker_id, h.name
) SELECT hid, hname, c_count
    FROM challenges_data
    WHERE c_count >= mc_count OR gc_count = 1
    ORDER BY c_count DESC, hid ASC;