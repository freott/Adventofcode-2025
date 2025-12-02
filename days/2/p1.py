def run(data: str, *args) -> int:
  ranges = data.split(',')
  
  hits = 0
  for range_str in ranges:  
    start, end = map(int, range_str.split('-'))
    
    for i in range (start, end + 1):
      no_as_str = str(i)
      str_length = len(no_as_str)
      if str_length % 2 != 0: continue
      
      mid = str_length // 2
      left = no_as_str[:mid]
      right = no_as_str[mid:]
      if left == right: hits += i
    
  return hits