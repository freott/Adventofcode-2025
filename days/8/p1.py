
from itertools import combinations
from math import prod

def run(data: str, *args) -> int:
  distances = []
  for n1, n2 in combinations(data.splitlines(), 2):
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
  
  node_map: dict[str, int] = {}
  circuit_map: dict[int, list[str]] = {}
  connections = 0
  iterator = 0
  connections_count = 10 if args[0] else 1000
  while connections < connections_count:
    _, n1, n2 = sorted_distances[iterator]
    if n1 in node_map and n2 in node_map:
      id = node_map[n1]
      id2 = node_map[n2]
      if (id == id2): 
        iterator += 1
        connections += 1
        continue
      circuit_map[id].extend(circuit_map[id2])
      del circuit_map[id2]
      for node_id in circuit_map[id]:
        node_map[node_id] = id
        
    elif n1 in node_map:
      id = node_map[n1]
      node_map[n2] = id
      circuit_map[id].append(n2)
      
    elif n2 in node_map:
      id = node_map[n2]
      node_map[n1] = id
      circuit_map[id].append(n1)
      
    else:
      id = iterator
      circuit_map[id] = [n1, n2]
      node_map[n1] = id
      node_map[n2] = id
    connections += 1
    iterator += 1
    
  
  lengths = sorted(map(len, circuit_map.values()), reverse=True)
  return prod(lengths[:3])