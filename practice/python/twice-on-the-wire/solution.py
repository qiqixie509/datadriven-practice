def collapse_pings(pings):
  result = []
  for item in pings:
    if not result or item != result[-1]:
      result.append(item)
  return result
