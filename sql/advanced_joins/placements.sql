SELECT
    s.name
FROM friends f
JOIN packages p
ON p.id = f.id
JOIN packages p2
ON p2.id = f.friend_id
JOIN students s
ON s.id = f.id
WHERE p2.salary > p.salary
ORDER BY p2.salary;