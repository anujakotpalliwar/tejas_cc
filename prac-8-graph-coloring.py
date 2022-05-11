def addEdge(adj, v, w):
    adj[v].append(w)
    adj[w].append(v) 
    return adj
 
def graph_coloring(adj, V):
    result = [-1] * V
    result[0] = 0;
    avail = [False] * V
    for u in range(1, V):
         
        for i in adj[u]:
            if (result[i] != -1):
                avail[result[i]] = True
 
        cr = 0
        while cr < V:
            if (avail[cr] == False):
                break
             
            cr += 1
             
        result[u] = cr
 
        for i in adj[u]:
            if (result[i] != -1):
                avail[result[i]] = False
 
    for u in range(V):
        print("Vertex", u, " --->  Color", result[u])
 
n = int(input("Enter number of vertices : "))
c = int(input("Enter number of colors : "))

edges=int(input("Enter numberof edges"))
gr=[[] for i in range(n)]
print("Enter edges : ")

for i in range(edges):
   u=int(input("u "))
   v=int(input("v "))
   addEdge(gr,u,v)

print("Coloring of graph 1 ")
graph_coloring(gr, n)
