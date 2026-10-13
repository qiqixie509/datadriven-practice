with grouped_table as (
  select
    lower(provider) as provider,
    date_format(bill_date, 'YYYY-MM') as month,
    sum(amount) as total
  from cloud_costs
  group by 1,2
  order by 2
)

select
  month,
  coalesce(sum(case when provider='aws' then total end), 0) as aws_total,
  coalesce(sum(case when provider='gcp' then total end), 0) as gcp_total,
  coalesce(sum(case when provider='azure' then total end), 0) as azure_total
from 
  grouped_table
group by 1
