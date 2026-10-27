from pyspark.sql import functions as F

base_price = (
  transactions.groupBy("product_id")
  .agg(
    F.min(F.col("total_amount")).alias("base_price")
    )
  )
result = (
  base_price.withColumn("avg_price", F.avg("base_price").over(Window.paritionBy()))
  .filter(F.col("base_price") > F.col("avg_price"))
  .select("product_id", "base_price")
  )
return result
