with rank_deploy as (
  select
    svc_name,
    row_number() over (
      partition by svc_name
      order by deploy_at desc
    ) as rn,
    version,
    dur_secs
  from deploy_logs
)
select 
  svc_name,
  version,
  dur_secs
from rank_deploy
where rn = 1
