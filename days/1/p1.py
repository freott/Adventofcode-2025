
def run(data: str, *args) -> int:
  rows = data.split('\n')
  
  pointer = 50
  zero_counts = 0
  for row in rows:
    direction = row[0]
    steps = int(row[1:])
  
    if direction == 'L':
      pointer = pointer - steps
    else:
      pointer = pointer + steps
    
    while pointer > 99:
      pointer -= 100
    while pointer < 0:
      pointer += 100
    
    if pointer == 0:
      zero_counts += 1
  return zero_counts