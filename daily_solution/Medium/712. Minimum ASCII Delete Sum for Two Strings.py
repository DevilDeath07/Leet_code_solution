class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # helper: compute total ASCII sum of a string
        def find_asci(s):
            return sum(ord(ch) for ch in s)

        m, n = len(s1), len(s2)
        # dp[i][j] = max ASCII sum of common subsequence of s1[:i], s2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # total ASCII sum of both strings
        total = find_asci(s1) + find_asci(s2)
        # subtract twice the common subsequence sum
        return total - 2 * dp[m][n]
