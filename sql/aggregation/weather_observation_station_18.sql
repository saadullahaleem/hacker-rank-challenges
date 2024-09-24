SELECT
    CAST(ABS(MAX(lat_n) - MIN(lat_n)) + ABS(MAX(long_w) - MIN(long_w)) AS DECIMAL(10, 4))
FROM
    station;