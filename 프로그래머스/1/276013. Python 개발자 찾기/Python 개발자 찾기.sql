-- 코드를 작성해주세요
select ID,EMAIL,FIRST_NAME, LAST_NAME
from DEVELOPER_INFOS
where SKILL_1 IN ('Python') or SKILL_2 IN ('Python') or SKILL_3 IN ('Python')
order by ID;