def read(data: str):
  rows = data.split('\n')
  batteries = []
  for row in rows:
    battery = {}
    for i, char in enumerate(row):
      digit = int(char)
      battery.setdefault(digit, []).append(i)
    batteries.append(battery)
  return batteries

def getHighest(battery: dict[int, list[int]]):
    for i in range(9, 0, -1):
      first = battery.get(i, [None])[0]
      if first == None: continue
      for n in range(9, 0, -1):
        second = battery.get(n, [None])[-1]
        if second == None: continue
        if second > first: 
          return int(str(i) + str(n))
        

def run(data: str, *args) -> int:
  batteries = read(data)
  sum = 0
  for battery in batteries:
    highest = getHighest(battery)
    sum += highest
  return sum