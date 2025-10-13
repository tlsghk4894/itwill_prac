# -- 코드를 입력하세요
SELECT u.user_id, nickname, concat(u.city,' ',u.street_address1,' ',u.street_address2) '전체주소',concat(left(u.tlno,3),'-',substring(u.tlno,4,4),'-',substring(u.tlno,8,4))'전화번호'
from used_goods_board b, used_goods_user u
where b.writer_id = u.user_id 
group by b.writer_id
having count(b.writer_id)>=3
order by u.user_id desc;

# select u.user_id,u.tlno
# from used_goods_board b, used_goods_user u
# where b.writer_id= u.user_id
# group by writer_id
# having count(b.writer_id)>=3
# order by u.user_id desc;