select
  distinct owner_id
from api_tokens
where issued < '2025-07-01' and
(
  expires > '2025-07-01' 
  or expires is NULL
)
order by 1
