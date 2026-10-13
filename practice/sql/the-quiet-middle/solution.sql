with rank_jobs as (
  select
    job_id,
    job_name,
    dense_rank() over (
      order by rows_done desc
    ) as rnk
  from batch_jobs
)
select 
  job_name,
  rnk
from rank_jobs
where rnk >= 8 and rnk <= 10
