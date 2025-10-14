-- 코드를 입력하세요
#대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차
# select car_id  
#     from CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     where date_format(start_date, '%Y-%m') between '2022-08' and '2022-10'
#     group by car_id
#     having count(*)>=5

select month(start_date) month, car_id, count(*)records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where car_id in (select car_id  
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where date_format(start_date, '%Y-%m') between '2022-08' and '2022-10'
    group by car_id
    having count(*)>=5) and date_format(start_date, '%Y-%m') between '2022-08' and '2022-10'
group by month, car_id
having COUNT(*) <> 0
order by month, car_id desc;

