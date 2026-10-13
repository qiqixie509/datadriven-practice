with last_transactions as (
  select
    date_format(transaction_date, 'YYYY-MM') as month,
    sum(total_amount) as revenue,
    LAG(sum(total_amount)) over (
      order by date_format(transaction_date, 'YYYY-MM')
    ) as last_revenue
  from transactions
  group by 1
  order by 1
)
select 
  month,
  revenue,
  case 
    when last_revenue is not null and last_revenue <> 0 
      then round((revenue-round(last_revenue,2)) * 100.0 / last_revenue, 2)
    else NULL
  end as pct_change
from last_transactions
