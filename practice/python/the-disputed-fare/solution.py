def find_fare_pair(fares, target):
  seen = {}
  for j, fare in enumerate(fares):
    complement = target - fares[j]
    if complement in seen:
      return [seen[complement], j]
    if fare not in seen:
      seen[fare] = j
  return None
  
