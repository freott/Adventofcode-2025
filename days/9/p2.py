from itertools import combinations
from utils.print_grid import print_grid

type Map = dict[int, list[int]]

def assign(v1: int, v2: int, map: Map):
  if v1 not in map:
    map[v1] = [v2, v2]
  else:
    lv2, hv2 = map[v1]
    if v2 < lv2: map[v1][0] = v2
    if v2 > hv2: map[v1][1] = v2

def run(data: str, *args) -> int:
  cords = [
    list(map(int, row.split(',')))
    for row in data.splitlines() 
  ]
  # print(cords)
  
  x_map: dict[int, list[list[int]]] = {}
  y_map: dict[int, list[list[int]]] = {}
  
  max_x = 0
  steps: dict[tuple[int, int], int] = {}
  prev_x, prev_y = cords[0]
  wall_id_iterator = 0
  for x, y in cords[1:] + [cords[0]]:
    if x > max_x: max_x = x
    if x != prev_x:
      low, high = sorted([prev_x, x])
      for x_step in range(low, high + 1):
        steps[(x_step, y)] = wall_id_iterator
        # print('-', x_step, y)
      wall_id_iterator += 1
      prev_x = x
      
    if y != prev_y:
      low, high = sorted([prev_y, y])
      for y_step in range(low, high + 1):
        t = (x, y_step)
        if t not in steps: steps[t] = wall_id_iterator
        # print('|', x, y_step)
        wall_id_iterator += 1
      prev_y = y

  # print(steps)
    
  bad_cords = set()
  good_cords = set()
  half_x = max_x // 2
  def valid(x_range: range, y_range: range):
    for start_x in x_range:
      for y in y_range:
        c = (start_x, y)
        if c in steps: continue
        wall_hits = set()
        # r = (range(start_x, max_x + 1) 
        #      if start_x > half_x
        #      else range(0, start_x + 1)
        # )
        r = range(0, start_x + 1)
        for x in r:
          if (x,y) in steps: wall_hits.add(steps[(x,y)])
        if len(wall_hits) % 2 == 0: 
          return False
    return True
  
  def validate_square(lx: int, ly: int, rx: int, ry: int):
    low_x, high_x = sorted([lx, rx])
    low_y, high_y = sorted([ly, ry])
    x_range = range(low_x, high_x + 1)
    y_range = range(low_y, high_y + 1)
    if (not valid(x_range, range(low_y, low_y + 1))
      or not valid(x_range, range(high_y, high_y + 1))
      or not valid(range(low_x, low_x + 1), y_range)
      or not valid(range(high_x, high_x + 1), y_range)):
      return False
    return True
  
  results = []
  for (lx, ly), (rx, ry) in combinations(cords, 2):
    result = (abs(lx - rx) + 1) * (abs(ry - ly) + 1)
    results.append([result, (lx, ly), (rx, ry)])
  
  n = len(cords)
  tot = n * (n - 1) // 2
  lap = 1
  for result, (lx, ly), (rx, ry) in sorted(results, reverse=True):
    print('lap', lap, 'of', tot)
    print(result, lx, ly, rx, ry, max_x)
    lap += 1
    # if rx == 2 and ry == 3 and lx == 9 and ly == 5:
      # print('hej')
    # low_x, high_x = sorted([lx, rx])
    # low_y, high_y = sorted([ly, ry])
    # x_range = range(low_x, high_x + 1)
    # y_range = range(low_y, high_y + 1)
    if not validate_square(lx, ly, rx, ry): continue
        
    return result
  # return highest