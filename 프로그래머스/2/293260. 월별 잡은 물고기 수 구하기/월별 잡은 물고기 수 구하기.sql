select count(*) as 'fish_count', month(time) as 'MONTH'
from fish_info
group by MONTH
having fish_count>0
order by MONTH;