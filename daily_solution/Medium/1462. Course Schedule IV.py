//  Floyd Warshall Algorithm    //

class Graph:
    def __init__(self, edges, N):
        self.adjList = [[] for _ in range(N)]
        self.indegree = [0] * N
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.indegree[dest] = self.indegree[dest] + 1

class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        graph = Graph(prerequisites,numCourses)
        print(graph)
        result=[[False]*numCourses for _ in range(numCourses)]
        for i in prerequisites:
            result[i[0]][i[1]]=True

        for intermediate in range(numCourses):
            for src in range(numCourses):
                for target in range(numCourses):
                    result[src][target] = result[src][
                        target] or (result[src][intermediate]
                        and result[intermediate][target])

        answer=[]
        for i in queries:
            answer.append(result[i[0]][i[1]])
        return answer
