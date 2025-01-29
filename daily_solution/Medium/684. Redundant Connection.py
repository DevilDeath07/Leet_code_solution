class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n=len(edges)
        par=[i for i in range(n+1)]  #ith elements from 1 to n+1
        r=[1]*(n+1)

        def find(n):
            if n!=par[n]:
                par[n]=find(par[n])
            return par[n]
        
        def union(a,b):
            x=find(a)
            y=find(b)
            if x==y:
                return False
            if r[x]>r[y]:
                par[y]=x
                r[x]+=r[y]
            else:
                par[x]=y
                r[y]+=r[x]
            return True
        
        for i,j in edges:
            if not union(i,j):
                return [i,j]
