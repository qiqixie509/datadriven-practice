with agg as (
  select 
   ad_campaign,
   count(impression_id) as impressions,
   sum(revenue) as total_revenue,
   sum(clicked) as total_clicks
  from ad_impressions
  group by ad_campaign
)
select 
   ad_campaign,
   impressions,
   total_revenue,
   round((total_clicks * 100.0 / impressions) , 1) as ctr
from agg
where impressions > 15
order by round((total_clicks * 100.0 / impressions) , 1) desc, ad_campaign asc
