SELECT hour(datetime) as 'HOUR', count(animal_type) as 'count'
from animal_outs
group by HOUR
having HOUR between 9 and 19
order by HOUR;