# Write your MySQL query statement below

with cte as (
    select user_id, 
    max(event_date) as latest, 
    max(monthly_amount) as max_paid,
    COALESCE(
        SUM(CASE WHEN event_type = 'downgrade' THEN 1 END), 0) AS downgrade_count,
    datediff(max(event_date), min(event_date)) as total_days
    from subscription_events group by user_id
),

cte2 as (
    select * , row_number() over (partition by user_id order by event_date desc) as rn
    from subscription_events
)

select t1.user_id, t2.plan_name as current_plan,
t2.monthly_amount as current_monthly_amount, 
t1.max_paid as max_historical_amount, t1.total_days as days_as_subscriber 
from cte as t1 join cte2 as t2 on t1.user_id = t2.user_id
where t2.rn = 1
and (t2.monthly_amount / t1.max_paid) < 0.5
and t1.total_days >= 60 
and t1.downgrade_count >= 1
and t2.event_type <> 'cancel'
order by t1.total_days desc, t1.user_id 
