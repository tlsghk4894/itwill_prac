-- 코드를 작성해주세요
select t.item_id, i.item_name, i.rarity
from item_info i join item_tree t on i.item_id = t.item_id
where t.parent_item_id in (select item_id 
                           from item_info 
                           where rarity = 'RARE')
order by t.item_id desc;
# select * from item_info i join item_tree t on i.item_id = t.parent_item_id;