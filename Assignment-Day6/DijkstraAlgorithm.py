
edges = [
    (0,1), (0,2), (0,3),
    (1,4), (1,5),
    (2,5), (2,6),
    (3,6),
    (4,7),
    (5,7), (5,8),
    (6,8),
    (7,8)
]

n = 9

graph = {}

for i in range(n):
    graph[i] = []

for u, v in edges:
    graph[u].append((v, 1))   
    graph[v].append((u, 1))   

print("Adjacency List:")
for node in graph:
    print(node, ":", graph[node])


def dijkstra(graph, source):
    distance = {}
    visited = {}

    for node in graph:
        distance[node] = float('inf')
        visited[node] = False

    distance[source] = 0

    for i in range(len(graph)):

        min_dist = float('inf')
        min_vertex = -1

        for node in graph:
            if not visited[node] and distance[node] < min_dist:
                min_dist = distance[node]
                min_vertex = node

        if min_vertex == -1:
            break

        visited[min_vertex] = True

        for neighbor, weight in graph[min_vertex]:
            if not visited[neighbor]:
                if distance[min_vertex] + weight < distance[neighbor]:
                    distance[neighbor] = distance[min_vertex] + weight

    return distance


source = int(input("\nEnter source vertex: "))

result = dijkstra(graph, source)

print("\nShortest distances from source", source)

for node in result:
    print(source, "->", node, "=", result[node])

