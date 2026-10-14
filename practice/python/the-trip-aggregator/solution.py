def aggregate_trips(trips: list[dict]) -> list[dict]:
  # trips: [{'user_id': str, 'origin': str, 'destination': str, 'duration_hours': int}]
  users = {}
  for trip in trips:
    uid = trip['user_id']
    if uid not in users:
      users[uid] = {'total_hours': 0, 'destinations': set()}
    users[uid]['total_hours'] += trip['duration_hours']
    users[uid]['destinations'].add(trip['destination'])
  
  result = []
  for uid in sorted(users.keys()):
    entry = {
        "user_id": uid,
        "total_hours": users[uid]['total_hours'],
        "unique_destinations": len(users[uid]['destinations'])
      }
    result.append(entry)
  return result
