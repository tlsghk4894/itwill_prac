-- 코드를 입력하세요
SELECT c.car_id
from (select car_id,car_type 
      from CAR_RENTAL_COMPANY_CAR
     where car_type = '세단') c , (select history_id, car_id, month(start_date) from CAR_RENTAL_COMPANY_RENTAL_HISTORY where month(start_date)=10) h
where c.car_id = h.car_id
group by h.car_id
having h.car_id in (c.car_id) 
order by h.car_id desc;

# select c.car_id, c.car_type, daily_fee, options ,month(h.start_date)
#       from CAR_RENTAL_COMPANY_CAR c, CAR_RENTAL_COMPANY_RENTAL_HISTORY h
#      where car_type='세단' and c.car_id = h.car_id

# select * 
# from CAR_RENTAL_COMPANY_CAR c, CAR_RENTAL_COMPANY_RENTAL_HISTORY h
# where c.car_id = h.car_id and month(start_date) = 10 and c.car_type='세단'
