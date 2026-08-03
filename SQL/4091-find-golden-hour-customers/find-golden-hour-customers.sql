# Write your MySQL query statement below

with customer_stats as (
    select order_id, customer_id, 
    sum(case 
    when time(order_timestamp) between '11:00:00' and '14:00:00'
    or time(order_timestamp) between '18:00:00' and '21:00:00' 
    then 1 else 0 
    end) as peak_hour_orders, 
    count(*) as total_orders, 
    avg(order_rating) as avg_order_rating, 
    count(order_rating) as rated_orders from restaurant_orders 
    group by customer_id 
)

select customer_id, total_orders, 
round((peak_hour_orders / total_orders) * 100) as peak_hour_percentage, 
round(avg_order_rating,2) as average_rating
from customer_stats 
where (peak_hour_orders / total_orders) >= 0.6
and  total_orders >= 3
and (rated_orders /total_orders) >= 0.5
and avg_order_rating >= 4.0
order by avg_order_rating desc, customer_id desc

