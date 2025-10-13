-- 코드를 입력하세요
SELECT r.food_type, r.rest_id, r.rest_name, r.favorites
from rest_info r join (select rest_id,max(favorites) favorites,food_type
                      from rest_info
                      group by food_type) as m on r.food_type = m.food_type and r.favorites = m.favorites
group by food_type
order by food_type desc;
# select rest_id,max(favorites) favorites,food_type
#                       from rest_info
#                       group by food_type
