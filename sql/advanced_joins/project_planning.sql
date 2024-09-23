WITH project_boundaries AS (SELECT start_date,
                                   end_date,
                                   CASE
                                       WHEN start_date <= LAG(end_date) OVER (ORDER BY start_date)
                                           THEN 0
                                       ELSE 1
                                       END AS is_new_project
                            FROM projects),
     project_groups AS (SELECT start_date,
                               end_date,
                               SUM(is_new_project) OVER (ORDER BY start_date) AS project_id
                        FROM project_boundaries),
     project_summary AS (SELECT MIN(start_date) AS s_date,
                                MAX(end_date)   AS e_date,
                                COUNT(*)        AS num_days
                         FROM project_groups
                         GROUP BY project_id)
SELECT s_date, e_date
FROM project_summary
ORDER BY num_days ASC, s_date ASC;