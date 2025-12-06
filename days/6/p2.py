from math import prod

def read(data: str):
  rows = data.split('\n')
  ops = []
  last_row = rows.pop()
  ops = [
    (ch, i)
    for i, ch in enumerate(last_row)
    if ch in { '+', '*' }
  ]
  return ops, rows

def run(data: str, *args) -> int:
  ops, rows = read(data)
  
  result = 0
  end = len(rows[0])
  for op, start in reversed(ops):
    numbers = [
      int("".join([row[i] for row in rows]))
      for i in range(start, end)  
    ]
    result += sum(numbers) if op == '+' else prod(numbers)
    end = start - 1
    
  return result