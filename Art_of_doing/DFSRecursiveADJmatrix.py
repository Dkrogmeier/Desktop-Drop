adjMatrix = {1: [2,3], 2: [3, 4], 3: [2, 5], 4: [1], 5: [4, 5, 2]}

def DFSrecursive(graph, vertex, path = []):
    path += [vertex]
    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = DFSrecursive(graph, neighbor, path)
    return path

print(DFSrecursive(adjMatrix, 1))



def dfs_visit(g, i):
    i.color = Color.Gray

    temp = i.head
    while(temp != None):
        if(g.heads[temp.index_of_item].color == Color.White):
            dfs_visit(g, g.heads[temp.index_of_item])
        temp = temp.next
    i.color = Color.Black
    print(i.data)

def dfs(g):
    for i in range(0, g.number_of_vertices):
        g.heads[i].color = Color.White

    for i in range(0, g.number_of_vertices):
        if(g.heads[i].color == Color.White):
            dfs_visit(g, g.heads[i])

if __name__ == '__main__':
    g = list[7]

    g.add_edge(1, 2)
    g.add_edge(1, 5)
    g.add_edge(1, 3)
    g.add_edge(2, 6)
    g.add_edge(2, 4)
    g.add_edge(5, 4)
    g.add_edge(3, 4)
    g.add_edge(3, 7)

    dfs(g)
