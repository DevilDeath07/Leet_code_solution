class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [False] * n
        vis = [False] * n
        result = set()
        
        def dfs(node):
            if vis[node]:
                return safe[node]
            vis[node] = True
            for i in graph[node]:
                if i not in result and not dfs(i):
                    return False
            safe[node] = True
            return True
        
        for i in range(n):
            if not graph[i]:
                result.add(i)

        for i in range(n):
            if not vis[i]:
                dfs(i)

        return [i for i in range(n) if safe[i]]

