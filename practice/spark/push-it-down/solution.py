from pyspark.sql import functions as F

events = spark.table("user_events")   # 3 TB, partitioned by event_date

# The date arrives through a runtime subquery join, so the planner treats
# it as an opaque value it cannot push into the scan.
this_year = (
    events.filter(F.col("event_date") >= "2026-01-01")
  )
esult = this_year.groupBy("country").agg(F.count("*").alias("events"))
result
