select
    p.product_id,
    p.product_name,
    t.transaction_id
  from products p
  left join transactions t
  on p.product_id = t.product_id
  where t.transaction_id is NULL
