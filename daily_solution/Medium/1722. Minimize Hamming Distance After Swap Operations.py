from typing import List
from collections import Counter, defaultdict

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        
        # Build adjacency list
        graph = defaultdict(list)
        for a, b in allowedSwaps:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        result = 0
        
        def dfs(node, indices):
            visited[node] = True
            indices.append(node)
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, indices)
        
        # Find connected components
        for i in range(n):
            if not visited[i]:
                indices = []
                dfs(i, indices)
                
                # Compare source and target values in this component
                src_vals = [source[j] for j in indices]
                tgt_vals = [target[j] for j in indices]
                
                src_count = Counter(src_vals)
                tgt_count = Counter(tgt_vals)
                
                # Count mismatches
                for val in src_count:
                    diff = src_count[val] - tgt_count.get(val, 0)
                    if diff > 0:
                        result += diff
        
        return result
