def flatten(feed: list) -> list:
  result = []
  for item in feed:
    if isinstance(item, list):
      result.extend(flatten(item))
    else:
      result.append(item)
  return result
  
