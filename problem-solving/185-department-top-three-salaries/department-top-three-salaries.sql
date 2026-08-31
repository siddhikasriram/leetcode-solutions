# Write your MySQL query statement below


with t1 as (
    select id, name, salary, departmentId,
    dense_rank() over( partition by departmentId order by salary desc) as ranks
    from employee  
)

select d.name as Department, e.name as Employee, e.Salary from t1 as e join department as d 
on e.departmentId = d.id where e.ranks <=3