spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")

transactions = spark.table("transactions")
users = spark.table("users")

matched = transactions.join(users, "user_id", "inner")
result = matched.select("user_id", "transaction_date", "total_amount")
