-- 코드를 작성해주세요
select  distinct(i.id) , n.fish_name, i.length
from fish_info i, fish_name_info n, (select max(length) length, fish_type
                                    from fish_info      
                                    group by fish_type) m
where i.fish_type=m.fish_type and m.length = i.length and i.fish_type = n.fish_type
order by i.id