with union_costs as (
  select 
    region,
    date_format(bill_date, '%Y-%m') as event_date,
    -sum(amount) as amt
  from cloud_costs
  group by 1,2
  UNION ALL
  select 
    region,
    period as event_date,
    sum(amount) as amt
  from cost_allocs
  group by 1,2
),
merged_cost as (
    select
      region,
      event_date,
      sum(amt) as amt
    from union_costs
    group by 1,2
  )
select 
  region,
  event_date,
  amt,
  sum(amt) over (
    partition by region
    order by event_date
    rows between unbounded preceding and current row
  ) as running_balance
from merged_cost
