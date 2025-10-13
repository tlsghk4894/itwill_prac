-- 코드를 작성해주세요
# select distinct(e.id), count(*) over(partition by d.parent_id) as child_count
# from ecoli_data e , ecoli_data d
# where d.parent_id = e.id 


select e.id , count(d.parent_id) as child_count
from ecoli_data e left join ecoli_data d on e.id = d.parent_id
group by e.id
order by e.id

