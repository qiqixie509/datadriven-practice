select
  impression_time,
  revenue
from ad_impressions
order by 2 desc, 1 asc
limit 3
