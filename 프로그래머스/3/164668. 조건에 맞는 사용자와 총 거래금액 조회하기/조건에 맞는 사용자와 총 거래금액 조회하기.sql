-- 코드를 입력하세요
SELECT u.user_id, nickname, sum(price) total_sales
from used_goods_board b, used_goods_user u
where b.writer_id = u.user_id and b.status = 'DONE'
group by b.writer_id
having total_sales >=700000
order by total_sales