WITH RECURSIVE numbers(n) AS (
    SELECT 2  -- Start with 2, the smallest prime
    UNION ALL
    SELECT n + 1
    FROM numbers
    WHERE n < 1000  -- Generate up to 1000
),
primes AS (
    SELECT n AS prime
    FROM numbers n1
    WHERE NOT EXISTS (
        SELECT 1
        FROM numbers n2
        WHERE n2.n > 1 AND n2.n < n1.n AND n1.n % n2.n = 0
    )
)
SELECT GROUP_CONCAT(prime ORDER BY prime SEPARATOR '&')
FROM primes;