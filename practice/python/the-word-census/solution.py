def build_frequency_tree(text: str) -> dict:
  mapping = {}
  arr = text.split()
  for item in arr:
      item = item.lower()
      mapping[item] = mapping.get(item, 0) + 1
  sorted_mapping = dict(sorted(mapping.items(), key=lambda x: x[1], reverse=True))
  return sorted_mapping
