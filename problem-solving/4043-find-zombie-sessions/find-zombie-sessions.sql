# Write your MySQL query statement below

with t1 as (
    select user_id, session_id,
    sum(case when event_type = 'scroll' then 1 else 0 end) as total_scrolls,
    sum(case when event_type = 'click' then 1 else 0 end) as total_clicks,
    sum(case when event_type = 'purchase' then 1 else 0 end) as total_purchase,
    MIN(CASE WHEN event_type = 'app_open' THEN event_timestamp END) AS open_time,
    MAX(CASE WHEN event_type = 'app_close' THEN event_timestamp END) AS close_time
    from app_events group by user_id 
)

select session_id, user_id, 
timestampdiff(minute, open_time, close_time) as session_duration_minutes,
total_scrolls as scroll_count 
from t1 
where total_scrolls >= 5 
and timestampdiff(minute, open_time, close_time) > 30
and (total_clicks / total_scrolls) < 0.2
and total_purchase = 0
order by total_scrolls desc, session_id 