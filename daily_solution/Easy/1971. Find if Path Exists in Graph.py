class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import deque
        graph = [[] for _ in range(n)] 
        for u, v in edges: 
            graph[u].append(v) 
            graph[v].append(u)
        if source == destination:
            return True
        visited = set()
        queue = deque([source])
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    queue.append(nei)
        return False
