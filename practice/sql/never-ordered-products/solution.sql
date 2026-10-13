with joined_table as (
  select
    p.product_id,
    p.product_name,
    t.transaction_id
  from products p
  left join transactions t
  on p.product_id = t.product_id
)
select 
  product_id, 
  product_name
from joined_table
where transaction_id is NULL
