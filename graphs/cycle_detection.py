'''
The following function finds a 
cycle in an undirected graph 
using BFS traversal.
'''
def dfs_check_undirected(node, adj, parent):
    visited[node] = 1

    for vertex in adj[node]:
        if visited[vertex] == 0:
            if dfs_check(vertex, adj, node):
                return

        else if (vertex != parent):
            return True

    return False

def bfs_directed_graph(node, adj, parent):
    visited[node] = 1
    

def dfs_check_directed(node, adj):
    visited[node] = 1
    dfsVisited[node] = 1

    for neighbor in adj[node]:
        if visited[neighbor] == 0:
            if dfs_check_directed(neighbor, adj):
                return True

        elif dfsVisited[neighbor]:
            return True

    dfsVisited[node] = 0
    return False

        
        
def bfs_check_undirected(node, adj):
    queue = [(node, -1)]

    while queue:
        curr_node, prev_node = queue.pop(0)
        if visited[curr_node] == 1:
            continue
        visited[curr_node] = 1

        for neighbor in adj[curr_node]:
            if visited[neighbor] == 1 and neighbor != prev_node:
                return False

            queue.append((neighbor, curr_node))
        
    return True