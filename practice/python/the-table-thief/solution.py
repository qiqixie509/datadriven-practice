import re
def extract_table_names(sql):
  pattern = r'(?:FROM|JOIN)\s+(\w+)'
  names = re.findall(pattern, sql, flags=re.IGNORECASE)
  return sorted(set(names))
