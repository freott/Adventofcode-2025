def read(data: str):
  rangesStr = data.split('\n\n')[0]
  ranges = [
    tuple(map(int, range.split('-'))) 
    for range in rangesStr.split('\n')
  ]
  return ranges

def run(data: str, *args) -> int:
  ranges = read(data)
  
  normalized_ranges = []
  (lo, hi), *sorted_ranges = sorted(ranges)
  for next_lo, next_hi in sorted_ranges:
    if next_lo > hi: 
      normalized_ranges.append((lo, hi))
      lo, hi = next_lo, next_hi
      continue
    if next_hi > hi: hi = next_hi
      
  normalized_ranges.append((lo, hi))
  
  return sum(hi - lo + 1 for lo, hi in normalized_ranges)