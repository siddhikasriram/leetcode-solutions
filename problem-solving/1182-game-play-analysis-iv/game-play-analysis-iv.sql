# Write your MySQL query statement below

WITH t1 AS (
    SELECT 
        player_id,
        MIN(event_date) AS first_login
    FROM activity
    GROUP BY player_id
),

t2 AS (
    SELECT 
        a.player_id,
        a.event_date,
        t1.first_login,
        LEAD(a.event_date) OVER (
            PARTITION BY a.player_id 
            ORDER BY a.event_date
        ) AS next_login
    FROM activity a
    JOIN t1
        ON a.player_id = t1.player_id
),
t3 as (
    select player_id from t2 
    where datediff(next_login, event_date) = 1 and event_date = first_login
)

select round(count(distinct player_id) / (select count(distinct player_id) from activity ),2) as fraction from t3
