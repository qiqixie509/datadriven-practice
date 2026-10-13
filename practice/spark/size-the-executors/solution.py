# Config A - dies in GC storms:
#   spark-submit --executor-memory 64g --executor-cores 16 --num-executors 50
#
# Config B - broadcast OOM (2.1 GB lookup + JVM overhead exceeds heap):
#   spark-submit --executor-memory 4g --executor-cores 1 --num-executors 800
#
# Cluster: 50 nodes, 128 GB RAM and 32 cores per node.
# Write the sizing that survives both failure modes.
BROADCAST_GB=2.1

by_user = Window.orderby("user_id")

candidates = (
    spark.table("users")
    .select(F.row_number().over(by_user).alias("cores_per_executor"))
    .where(F.col("cores_per_executor") <= 5)
    .withColumn("executors_per_node", F.floor(F.lit(31) / F.col("cores_per_executor")))
  )
sized = candidates.withColumn(
  "heap_gb", F.floor(F.lit(127) / F.col("executors_per_node")) - 2
)

result = (
  sized
  .where(F.col("heap_gb") >= 3 * BROADCAST_GB)
  .select(
    "cores_per_executor",
    "executors_per_node",
    "heap_gb",
    (F.lit(50) * F.col("executors_per_node")).alias("total_executors"),
  )
)
