-- 코드를 작성해주세요
select i.item_id, i.item_name, i.rarity
from item_info i, item_tree t
where i.item_id = t.item_id and i.item_id not in (select parent_item_id
                                                 from item_tree
                                                 where parent_item_id is not null)
order by item_id desc;