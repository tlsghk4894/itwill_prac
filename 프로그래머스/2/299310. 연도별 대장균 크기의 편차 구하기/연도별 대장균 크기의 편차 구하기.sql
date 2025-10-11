select year(differentiation_date) YEAR, (select max(size_of_colony)
                                         from ecoli_data d
                                         where year(e.differentiation_date) = year(d.differentiation_date)) - size_of_colony YEAR_DEV, ID
from ecoli_data e
order by YEAR, YEAR_DEV