SELECT o.user_id, o.product_id
from online_sale o join online_sale s on o.user_id=s.user_id and o.product_id=s.product_id
where o.online_sale_id !=s.online_sale_id
group by o.user_id, o.product_id
order by o.user_id , o.product_id desc;

# select * 
# from online_sale
# order by user_id;