from collections import deque


class HitCounter:
  def __init__(self):
    self.hits = deque()
  def hit(self, timestamp: int):
    self.hits.append(timestamp)
  def get_hits(self, timestamp: int) -> int:
    cutoff = timestamp - 299
    while self.hits and self.hits[0] < cutoff:
      self.hits.popleft()
    return len(self.hits)
  
  
def event_window(operations, arguments):
  # Replay each operation against a single HitCounter instance.
  # "HitCounter" -> construct (append None); "hit" -> record (append None);
  # "get_hits" -> append the returned count.
  counter = None
  result = []
  for op, arg in zip(operations, arguments):
    if op == 'HitCounter':
      counter = HitCounter()
      result.append(None)
    elif op == 'hit':
      counter.hit(*arg)
      result.append(None)
    elif op == 'get_hits':
      result.append(counter.get_hits(*arg))
  return result
