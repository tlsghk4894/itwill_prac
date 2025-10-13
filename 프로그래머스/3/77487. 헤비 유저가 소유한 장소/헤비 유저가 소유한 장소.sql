-- 코드를 입력하세요
SELECT p.id, p.name, p.host_id
from places p ,(select id,name,host_id
     from places
     group by host_id
    having count(host_id)>=2) as place
where place.host_id = p.host_id
order by id