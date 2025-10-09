class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        f = [0] * n  # earliest free time for each wizard

        for x in mana:
            now = f[0]
            for i in range(1, n):
                now = max(now + skill[i-1] * x, f[i])
            f[n-1] = now + skill[n-1] * x
            for i in reversed(range(n-1)):
                f[i] = f[i+1] - skill[i+1] * x

        return f[-1]  
