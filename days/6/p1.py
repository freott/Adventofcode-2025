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
  end = None
  for op, start in reversed(ops):
    numbers = [int(row[start:end]) for row in rows]
    result += (
      sum(numbers) 
      if op == '+' 
      else prod(numbers)
    )
    end = start
  return result