from collections import Counter

def dice_roll_scoring(dice: list[int]):
  counts = Counter(dice)
  value_counts = sorted(counts.values(), reverse=True)
  total = sum(dice)
  if value_counts == [5]:
    return 50
  elif value_counts[0] == 4:
    return 40
  elif value_counts == [3,2]:
    return 25
  else:
    return total
