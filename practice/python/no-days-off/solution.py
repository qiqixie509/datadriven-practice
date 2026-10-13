def find_streak_users(activities: list[dict], min_streak: int = 3) -> list[str]:
  mapping = {}
  result = []
  for row in activities:
    key = row.get('user_id')
    date = row.get('date')
    if key not in mapping:
      mapping[key] = set()
    mapping[key].add(date)
  length_mapping = {key: len(dates) for key, dates in mapping.items()}
 
  for k,v in length_mapping.items():
    if v >= min_streak:
      result.append(k)
  return sorted(result)
    
