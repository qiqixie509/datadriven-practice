with joined_table as (
  select 
    ae.alert_id,
    ae.status,
    ai.ad_campaign
  from ad_impressions ai
  left join alert_events ae
  on DATE_FORMAT(ae.fired_at, '%Y-%m-%d %H:00:00') = DATE_FORMAT(ai.impression_time, '%Y-%m-%d %H:00:00')
  where ae.fired_at is not NULL
)
select
  ad_campaign,
  count(distinct alert_id) as alert_count,
  count(distinct case when status = 'resolved' then alert_id end) as resolved_count
from joined_table
group by 1
