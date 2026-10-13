from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

# After filter: 2 GB of data. Target file size ~200 MB -> 10 files.
# coalesce(N) merges partitions without a full shuffle (narrow dependency).
# repartition(N) would trigger a full shuffle: unnecessary here since we
# are only reducing partition count, not redistributing keys.

flagged = (
  spark.table("transactions")
  .filter(col("total_amount") > 500)
  .coalesce(10)   # 2 GB / 10 = 200 MB per file, Athena-friendly
)

flagged.write \
  .mode("overwrite") \
  .parquet("s3://exports/flagged_transactions/")
