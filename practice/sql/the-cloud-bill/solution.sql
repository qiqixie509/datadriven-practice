select
  date_format(bill_date, 'YYYY-MM') as month,
  coalesce(sum(case when lower(provider)='aws' then amount end), 0) as aws_total,
  coalesce(sum(case when lower(provider)='gcp' then amount end), 0) as gcp_total,
  coalesce(sum(case when lower(provider)='azure' then amount end), 0) as azure_total
from 
  cloud_costs
group by 1
