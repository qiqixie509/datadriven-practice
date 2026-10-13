from collections import OrderedDict

class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = OrderedDict()
    
  def get(self, key: int) -> int:
    if key not in self.cache:
      return -1
    self.cache.move_to_end(key)
    return self.cache[key]
  
  def put(self, key:int, value:int):
    if key in self.cache:
      self.cache.move_to_end(key)
    self.cache[key] = value
    if len(self.cache) > self.capacity:
      self.cache.popitem(last=False)
    return None
  
def the_eviction_policy(operations):
    # operations[0] is ['LRUCache', capacity]; the rest are
    # ['put', key, value] or ['get', key].
    # Define an LRUCache class with O(1) get/put, replay the ops,
    # and return the list of results (None for constructor/put,
    # the value or -1 for get).
    cache = None
    results = []
    for opt in operations:
      name = opt[0]
      if name == "LRUCache":
        cache = LRUCache(opt[1])
        results.append(None)
      elif name == "put":
        results.append(cache.put(opt[1], opt[2]))
      elif name == "get":
        results.append(cache.get(opt[1]))
    return results
      
  
