from pyspark.sql import functions as F

results = (
  ad_impressions.groupBy("ad_campaign")
  .agg(
    F.count("impression_id").alias("impressions"),
    F.sum("revenue").alias("total_revenue"),
    F.round(F.sum("clicked") * 100.0 / F.count("impression_id"), 1).alias("ctr")
    )
  .filter(F.col("impressions") > 15)
  .orderBy(F.col("ctr").desc(), F.col("ad_campaign").asc())
)
