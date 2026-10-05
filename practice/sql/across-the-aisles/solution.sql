with joined_table as (
  select
    t.product_id,
    p.category,
    t.user_id
   from transactions t
   left join products p
   on t.product_id = p.product_id
   where p.category is not NULL
)
select
  user_id,
  count(distinct category) as category_count
from joined_table
group by user_id
order by count(distinct category) desc, user_id asc
