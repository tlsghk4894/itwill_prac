SELECT book_id, date_format(PUBLISHED_DATE,'%Y-%m-%d') as 'PUBLISHED_DATE'
from book
where year(PUBLISHED_DATE)= 2021 and category ='인문'
order by PUBLISHED_DATE;
# select *
# from book;
