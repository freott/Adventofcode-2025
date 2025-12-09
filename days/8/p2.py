
from itertools import combinations
from math import prod

def run(data: str, *args) -> int:
  distances: list[tuple[int, str, str]] = []
  rows = data.splitlines()
  for n1, n2 in combinations(rows, 2):
    x1, y1, z1 = n1.split(',')
    x2, y2, z2 = n2.split(',')
    dx = int(x1) - int(x2)
    dy = int(y1) - int(y2)
    dz = int(z1) - int(z2)
    distances.append((
      dx*dx + dy*dy + dz*dz, 
      n1,
      n2
    ))
  sorted_distances = sorted(distances, key= lambda x: x[0])
  
  total_nodes_count = len(rows)
  nodes_count = 0
  node_map: dict[str, int] = {}
  circuit_map: dict[int, list[str]] = {}
  iterator = 0
  result = None
  while result is None:
    _, n1, n2 = sorted_distances[iterator]
    if n1 in node_map and n2 in node_map:
      id = node_map[n1]
      id2 = node_map[n2]
      if (id == id2): 
        iterator += 1
        continue
      circuit_map[id].extend(circuit_map[id2])
      del circuit_map[id2]
      for node_id in circuit_map[id]:
        node_map[node_id] = id
        
    elif n1 in node_map:
      id = node_map[n1]
      node_map[n2] = id
      circuit_map[id].append(n2)
      nodes_count += 1
      
    elif n2 in node_map:
      id = node_map[n2]
      node_map[n1] = id
      circuit_map[id].append(n1)
      nodes_count += 1
      
    else:
      id = iterator
      circuit_map[id] = [n1, n2]
      node_map[n1] = id
      node_map[n2] = id
      nodes_count += 2
    if total_nodes_count == nodes_count:
      result = int(n1.split(',')[0]) * int(n2.split(',')[0])
    iterator += 1
    
  return result