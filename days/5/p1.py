def read(data: str):
  rangesStr, ingredientsStr = data.split('\n\n')
  ranges = [
    tuple(map(int, range.split('-'))) 
    for range in rangesStr.split('\n')
  ]
  ingredients = map(int, ingredientsStr.split('\n'))
  return ranges, ingredients

def run(data: str, *args) -> int:
  ranges, ingredients = read(data)
  
  freshCount = 0
  for ingredient in ingredients:
    if any(lo <= ingredient <= hi for lo, hi in ranges): 
      freshCount += 1
      continue

  return freshCount