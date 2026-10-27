from pyspark.sql import functions as f

window = Window.partitionBy("topic").orderBy("offset")
result = (
  stream_msgs
  .withColumn("prev_offset", F.lag(F.col("offset"), 1).over(window))
  .withColumn("msg_rank", F.dense_rank().over(window))
  .withColumn("msg_row_num", F.row_number().over(window))
  .filter(F.col("prev_offset").isNotNull())
  .select("topic", "offset", "prev_offset", "msg_rank", "msg_row_num")
  )
