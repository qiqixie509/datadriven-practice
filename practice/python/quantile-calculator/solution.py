def quantile_calculator(data: list[float], percentile: float):
  sorted_data = sorted(data)
  n = len(data)
  pos = percentile / 100.0 * (n-1)
  lower = int(pos)
  upper = lower + 1
  print(f"lower = {lower}, upper = {upper}")
  if upper >= n:
    return sorted_data[lower]
  fraction = pos-lower
  result = sorted_data[lower] + fraction * (sorted_data[upper] - sorted_data[lower])
  return result
