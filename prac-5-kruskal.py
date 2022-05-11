n = int(input("Enter Total no. of Vertices"))
graph = []

def findPar(parent, node):
    if parent[node] == node:
        return node
    else:
        return findPar(parent, parent[node])


def union(parent, rank, x, y):
   
    x = findPar(parent, x)
    y = findPar(parent, y)
    if rank[x] == rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y


def add_edge(graph, u, v, w):
    graph.append([u, v, w])


def kruskal(graph):
    result = []
    parent = []
    rank = []

    graph = sorted(graph, key=lambda item: item[2])
    for i in range(n+1):
        parent.append(i)
        rank.append(0)
    j = 0
    edges = 0
    while edges < n-1:
        u, v, w = graph[j]
        j = j+1
        x = findPar(parent, u)
        y = findPar(parent, v)
        if x != y:
            result.append([u, v, w])
            union(parent, rank, u, v)
            edges = edges+1
    print(result)


add_edge(graph, 1, 4, 1)
add_edge(graph, 1, 2, 2)
add_edge(graph, 2, 3, 3)
add_edge(graph, 2, 4, 3)
add_edge(graph, 1, 5, 4)
add_edge(graph, 3, 4, 5)
add_edge(graph, 2, 6, 7)
add_edge(graph, 3, 6, 8)
add_edge(graph, 4, 5, 9)

kruskal(graph)
