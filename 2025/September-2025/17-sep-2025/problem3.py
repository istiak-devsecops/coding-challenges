# Build an adjacency list for a graph:
from collections import defaultdict
edges = [("a","b"),("a","c"),("b","d"),("c","d"),("d","e")]

graph = defaultdict(list)

for u,v in edges:
    graph[v].append(u)
    graph[u].append(v)

for node, neighb in graph.items():
    print(f"{node} : {neighb}")