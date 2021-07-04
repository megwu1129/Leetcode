class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0]*len(graph)
        for i in range(len(graph)):
            if visited[i] == 0 and len(graph[i]) !=0: # not visited and has edges
                visited[i] = 1
                q = collections.deque([i])
                while len(q) != 0:
                    curr = q.popleft()
                    for neighbor in graph[curr]:
                        if visited[neighbor] ==  0:
                            visited[neighbor] = -visited[curr]
                            q.append(neighbor)
                        elif visited[neighbor] == visited[curr]:
                            return False
        return True 
