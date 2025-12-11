from functools import reduce
from itertools import count

def read(row: str):
  lights_str, rest = row.split('] ')
  wiring_str = rest.split(' {')[0]
  expected_str = (lights_str[1:]
    .replace('.', '0')
    .replace('#', '1')
  )
  expected_len = len(expected_str)
  expected = int(expected_str, 2)
  button_groups = [
    list(map(int, button[1:-1].split(',')))
    for button 
    in wiring_str.split(' ')
  ]
  buttons = [
    reduce(
      lambda acc, 
      light: acc ^ (1 << (expected_len - 1 - light)), 
      button_numbers, 0
    )
    for button_numbers in button_groups
  ]
  return expected, buttons
  
def calcClicks(expected: int, buttons: list[int]):
  results = set([0])
  for i in count(start=1):
    prev_results = results.copy()
    results.clear()
    for current in prev_results:
      needed = current ^ expected
      for button in buttons:
        if button & needed == 0: continue
        result = current ^ button
        if result == expected: return i
        results.add(result)
  return 0

def run(data: str, *args) -> int:
  return sum([
    calcClicks(*read(row))
    for row in data.splitlines()
  ])