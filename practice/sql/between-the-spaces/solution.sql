select
  msg_id,
  length(content) - length(replace(content, ' ', '')) + 1 as word_count
from  chat_msgs
