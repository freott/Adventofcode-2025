def read(data: str):
  start_x = 0
  splitters = set()
  rows = data.splitlines()
  for y, row in enumerate(rows):
    for x, cell in enumerate(row):
      if cell == 'S': start_x = x
      if cell == '^': splitters.add((y, x))      
  return start_x, splitters, len(rows)

def run(data: str, *args) -> int:
  start_x, splitters, end_y = read(data)
  
  beams = { start_x: 1 }
  for y in range(1, end_y):
    copied_beams = beams.copy()
    beams.clear()
    for beam, timelines in copied_beams.items():
      if (y, beam) in splitters:
        left, right = beam - 1, beam + 1
        beams[left] = beams.get(left, 0) + timelines
        beams[right] = beams.get(right, 0) + timelines
      else:
        beams[beam] = beams.get(beam, 0) + timelines
  
  return sum([timeline for timeline in beams.values()])