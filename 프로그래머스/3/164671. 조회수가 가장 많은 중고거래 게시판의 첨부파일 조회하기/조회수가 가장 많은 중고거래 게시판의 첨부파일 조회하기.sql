-- 코드를 입력하세요
SELECT concat('/home/grep/src/',f.board_id,'/',f.file_id, f.file_name,f.file_ext ) as 'file_path'
from used_goods_board b, used_goods_file f, (select board_id, max(views) views from used_goods_board) m
where b.board_id = f.board_id and b.views = m.views
order by f.file_id desc;
# select * 
# from used_goods_file
# where board_id = 'b0008'