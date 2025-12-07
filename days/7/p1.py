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
  
  splits = 0
  next_beams = set([start_x])
  for y in range(1, end_y):
    beams = list(next_beams)
    for beam in beams:
      if (y, beam) in splitters:
        splits += 1
        next_beams.remove(beam)
        next_beams.add(beam - 1)
        next_beams.add(beam + 1)
  return splits