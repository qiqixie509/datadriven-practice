with base_price as (
  select 
    product_id,
    min(total_amount) as base_price
  from transactions
  group by 1
),
avg_base_price as (
  select 
    avg(base_price) as avg_price
  from base_price
  )
select
  product_id,
  base_price
from base_price b, avg_base_price a
where b.base_price > a.avg_price
