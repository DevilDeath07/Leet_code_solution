class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a - 1].append(b - 1)
            g[b - 1].append(a - 1)

        result =0
        color=[0]*n

        def biparti_graph(a,b):
            color[a]=b
            components.append(a)
            for i in g[a]:
                if (not color[i] and not biparti_graph(i,-1*b) or color[i]==b):
                    return False
            return True

        def depth(a):
            visit=[0]*n 
            que=deque([a])
            visit[a]=1
            dep=0
            while que:
                for _ in range(len(que)):
                    for i in g[que.popleft()]:
                        if not visit[i]:
                            que.append(i)
                            visit[i]=1
                dep+=1
            return dep
        

        for i in range(n):
            if not color[i]:
                components=[]
                if not biparti_graph(i,1):
                    return -1
                result += max(depth(i) for i in components)
        return result      
