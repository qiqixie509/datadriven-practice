from pyspark.sql import SparkSession

calls = spark.table("api_calls")

status_counts = (
  calls
  .groupBy("status")
  .agg(F.count("*").alias("call_count"))
)
