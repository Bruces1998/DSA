'''
Cycle detection using DFS 
and BFS in undirected graphs.
'''

def cycleDetection(edges, n, m):
    
    # Write your code here.
    # Return "Yes" if cycle id present in the graph else return "No".

    adj = defaultdict(list)
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    def dfs(node, adj, visited, prev):
            
        visited[node] = 1
        for neighbor in adj[node]:
            if visited[neighbor] == 0:
                if dfs(neighbor, adj, visited, node):
                	return True
            
            else:
                if neighbor != prev:
                	return True
        return False


        
    def bfs(node, adj, visited):
        queue = [(node, -1)]
        
        while queue:
            curr, prev = queue.pop(0)
            if visited[curr] == 1:
                continue
            
            visited[curr] = 1
            
            for neigh in adj[curr]:
                if visited[neigh] == 1 and neigh != prev:
                    return True
                
                queue.append((neigh, curr))
                
        return False

    visited = [0 for _ in range(n+1)]
    for i in range(1, n+1):
      
        if visited[i] == 0 and bfs(i, adj, visited):
            return "Yes"
        
    return "No"


