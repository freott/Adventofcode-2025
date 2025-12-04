def read(data: str):
  rows = data.splitlines()
  papers = set()
  for y, row in enumerate(rows):
    for x, cell in enumerate(row):
      if cell == '@': papers.add((y, x))
  return papers

dd = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, -1], [-1, 1], [1, 1], [1, -1]]
def run(data: str, *args) -> int:
  papers = read(data)
  
  valid_rolls = 0  
  for y, x in papers:
    neighbors = 0
    for dir in range(8):
      next_y = y + dd[dir][0]
      next_x = x + dd[dir][1]
      if (next_y, next_x) in papers: neighbors += 1
    
    if neighbors < 4: valid_rolls += 1
      
  return valid_rolls