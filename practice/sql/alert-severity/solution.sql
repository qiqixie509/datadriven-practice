with nest_result as (
  select
    topic,
    offset,
    LAG(offset, 1) over (
      partition by topic
      order by offset asc
    ) as prev_offset,
    DENSE_RANK() over (
      partition by topic
      order by offset
      ) as msg_rank,
    ROW_NUMBER() over (
      partition by topic
      order by offset
    ) as msg_row_num
  from stream_msgs
)
select * from nest_result 
where prev_offset is not NULL
