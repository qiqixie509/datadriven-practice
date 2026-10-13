def word_frequency_top_k(text: str, k: int) -> list:
  arr = text.split()
  mapping = {}
  for item in arr:
    mapping[item] = mapping.get(item, 0) + 1
  sorted_mapping = dict(
    sorted(mapping.items(), key=lambda x: (-x[1], x[0]))
  )
  print(sorted_mapping)
  result = list(sorted_mapping)[:k]
  return result
