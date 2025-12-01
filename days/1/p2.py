
def run(data: str, *args) -> int:
  rows = data.split('\n')
  
  pointer = 50
  zero_counts = 0
  for row in rows:
    direction = row[0]
    steps = int(row[1:])
    
    for _ in range(steps):
      if direction == 'L':
        pointer = pointer - 1
      else:
        pointer = pointer + 1
      
      if pointer > 99:
        pointer -= 100
      if pointer < 0:
        pointer += 100
        
      if pointer == 0: zero_counts +=1
      
  return zero_counts
