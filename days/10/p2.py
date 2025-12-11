from functools import reduce
from itertools import count

def read(row: str):
  buttons_str, joltage_str = row.split('] ')[1].split(' {')
  buttons = [
    tuple(map(int, button[1:-1].split(',')))
    for button 
    in buttons_str.split(' ')
  ]
  jolts = list(map(int, joltage_str[:-1].split(',')))
  return jolts, buttons

def makeClicks(
  jolts: list[int], 
  buttons: list[tuple[int, ...]], 
  incoming_clicks = 0,
):
  for jolt_i, jolt in sorted(enumerate(jolts), key=lambda x: x[1]):
    for clicks in range(jolt, 1, -1):
      lowest_clicks = 100_000
      for button_lights in [
        lights for lights in buttons 
        if jolt_i in lights 
        and all(jolts[light] >= clicks for light in lights)
      ]:
        new_jolts = [j - clicks if i in button_lights else j for i, j in enumerate(jolts)]
        if all(nj == 0 for nj in new_jolts):
          print('Success! returning', incoming_clicks + clicks)
          print(new_jolts)
          return incoming_clicks + clicks
        new_clicks = makeClicks(new_jolts, buttons, incoming_clicks + clicks)
        # if more_clicks > 0: return more_clicks
        if new_clicks < 100_000: lowest_clicks = new_clicks
      
      if lowest_clicks < 100_000: return lowest_clicks
  return False
          
  
def calcClicks(jolts: list[int], buttons: list[tuple[int, ...]]):
  # print('Going for', jolts)
  # print(sorted(buttons, key=lambda x: len(x), reverse=True))
  # print(sorted(jolts))
  res = makeClicks(jolts, sorted(buttons, key=lambda x: len(x), reverse=True))
  print(res)
  return res
  
  # clicks = 0
  # prev_results = { tuple(jolts) }
  # for i in range(len(jolts)):
  #   print(i, 'in', jolts)
  #   clicks += jolts[i]
  #   results = prev_results.copy()
  #   prev_results.clear()
  #   # Button click
  #   for button_lights in [b for b in buttons_lights if i in b]:
  #     # Prev result
  #     for prev_result in results:
  #       # Light in result
  #       result = list(prev_result)
  #       below_zero = False
  #       for light in button_lights:
  #         result[light] -= jolts[i]
  #         if result[light] < 0: 
  #           below_zero = True
  #           break
  #       if all(jolt == 0 for jolt in result): return clicks
  #       if not below_zero: prev_results.add(tuple(result))
  # return 0
      
      
      
  # results = set([tuple(jolts)])
  
  # for i in count(start=1):
  #   prev_results = results.copy()
  #   results.clear()
    
  #   for current in prev_results:
  #     for lights in buttons_lights:
  #       result = list(current)
  #       for light in lights:
  #         result[light] -= 1
  #       success = True
  #       for jolt in result:
  #         if jolt < 0: 
  #           success = False
  #           break
  #         if jolt > 0:
  #           results.add(tuple(result))
  #           success = False
  #           break
  #       if success: 
  #         print('returning', i, result)
  #         return i
        
  # return 0

def run(data: str, *args) -> int:
  return sum([
    calcClicks(*read(row))
    for row in data.splitlines()
  ])
    