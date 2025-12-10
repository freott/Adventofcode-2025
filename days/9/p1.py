from itertools import combinations


def run(data: str, *args) -> int:
  cords = [list(map(int, row.split(','))) for row in data.splitlines()]
  
  highest = 0
  for (lx, ly), (rx, ry) in combinations(cords, 2):
    result = (abs(lx - rx) + 1) * (abs(ry - ly) + 1)
    if result > highest: highest = result
    
  return highest