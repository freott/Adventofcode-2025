from pprint import pprint

def read(data: str):
  rows = data.split('\n')
  batteries = []
  for row in rows:
    index_groups = {}
    for i, char in enumerate(row):
      digit = int(char)
      index_groups.setdefault(digit, []).append(i)
    batteries.append([index_groups, len(row)])
  return batteries

def getHighest(battery: list[dict[int, list[int]], int]):
  index_groups, length = battery
  result = ''
  for result_i in range(12):
    remaining_digits = 12 - (result_i + 1)
    for i in range(9, 0, -1):
      vals = index_groups.get(i)
      digit_i = vals[0] if vals else None
      if digit_i == None: continue
      if digit_i >= length - remaining_digits: continue

      for key in index_groups:
        index_groups[key][:] = [x for x in index_groups[key] if x > digit_i]
      
      result += str(i)
      break
  return int(result)

def run(data: str, *args) -> int:
  batteries = read(data)
  sum = 0
  for battery in batteries:
    highest = getHighest(battery)
    sum += highest
  return sum