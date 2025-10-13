-- 코드를 작성해주세요
select s.id, case
when s.ranking <=total_count*0.25 then 'CRITICAL'
when s.ranking <=total_count*0.5 then 'HIGH'
when s.ranking <=total_count*0.75 then 'MEDIUM'
else 'LOW'
end as 'COLONY_NAME'
from (
    select id,size_of_colony, row_number() over (order by size_of_colony desc) as ranking,           count(id) over () as total_count
    from ecoli_data
    ) s 
order by s.id
