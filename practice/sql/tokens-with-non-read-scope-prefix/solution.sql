select count(distinct owner_id)
from api_tokens
where scope not like 'read%'
