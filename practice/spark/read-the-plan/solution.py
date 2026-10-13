orders = spark.table("retail_orders")
stores = spark.table("stores")

# stores is the small side: ship a copy to every executor so orders never moves
result = (
  orders
  .join(F.broadcast(stores), on="store_id", how="inner")
  .select("order_id", "amount", "store_name", "region")
)
