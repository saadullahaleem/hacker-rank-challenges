SELECT w.id, wp.age, w.coins_needed, w.power
FROM wands w
JOIN wands_property wp
ON w.code = wp.code
WHERE wp.is_evil = 0 AND w.coins_needed = (
    SELECT MIN(w2.coins_needed) FROM wands w2
    JOIN wands_property wp2 on w2.code = wp2.code
    WHERE wp.age = wp2.age AND w.power = w2.power
) ORDER BY w.power DESC, wp.age DESC;