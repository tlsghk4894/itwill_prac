-- 코드를 입력하세요
SELECT o.animal_id, o.name
from animal_ins i, animal_outs o
where i.animal_id=o.animal_id
order by datediff(o.datetime,i.datetime)+1 desc
limit 2;