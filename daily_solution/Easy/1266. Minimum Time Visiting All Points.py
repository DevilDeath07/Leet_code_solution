class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        def count_time_visit(start, end):
            s_1, s_2 = start
            t_1,t_2 = end
            return max(abs(s_1 - t_1), abs(s_2 - t_2))
        for i in range(len(points)-1):
            count += count_time_visit(points[i],points[i+1])
        return count
