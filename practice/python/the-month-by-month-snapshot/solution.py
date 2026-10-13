def monthly_sales_crosstab(records: list[dict]) -> list[dict]:
  totals: dict[str, dict[str, int]] = {}
  for rec in records:
    emp = rec.get('employee_id')
    key = rec.get('month')[:3].lower()
    amt = rec.get("sales_amount")
    months = totals.setdefault(emp, {})
    months[key] = months.get(key, 0) + amt
  result = []
  for emp in sorted(totals):
    row = totals[emp]
    row['employee_id'] = emp
    result.append(row)
  return result
