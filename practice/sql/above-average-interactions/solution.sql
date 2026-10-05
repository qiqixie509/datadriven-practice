with count_sessions as (
  select 
    user_id,
    count(*) as total_sessions
  from user_sessions
  group by 1
),
avg_session as (
  select
    avg(total_sessions) as avg_session
  from count_sessions
)
select 
  user_id,
  total_sessions
from count_sessions, avg_session
where total_sessions > avg_session
order by total_sessions desc, user_id asc
