def is_match(end: int, id_str: str) -> bool:
  left_str = id_str[0:end]
  left_len = len(left_str)
  remaining_str = id_str[end:]
  laps = len(remaining_str) // left_len
  
  for lap in range(laps):
    start = lap * left_len
    right_str = remaining_str[start:start+left_len]
    if left_str != right_str: return False
    
  return True
    
    
  

def run(data: str, *args) -> int:
  ranges = data.split(',')
  
  hits = 0
  for range_str in ranges: 
    start, end = map(int, range_str.split('-'))
    
    for id_no in range(start, end + 1):
      id_str = str(id_no)
      total_len = len(id_str)
      mid = total_len // 2
      for char_i in range(mid):
        compare_len = char_i + 1
        if total_len % compare_len != 0: continue
        
        if (is_match(compare_len, id_str)):
          hits += id_no
          break
        
        
        
    
  return hits