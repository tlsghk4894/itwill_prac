-- 코드를 입력하세요
SELECT car_id, round(avg(datediff(end_date, start_date)+1),1) average_duration
from car_rental_company_rental_history
group by car_id
having average_duration >=7
order by average_duration desc,car_id desc

# select car_id,round(avg(datediff(end_date,start_date)),1)
# from car_rental_company_rental_history 
# group by car_id
# having round(avg(datediff(end_date, start_date)),1)>=7
# order by car_id