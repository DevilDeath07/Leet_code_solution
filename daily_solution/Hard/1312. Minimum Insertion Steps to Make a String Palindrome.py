class Solution:
    def minInsertions(self, s: str) -> int:
        #find the longest palindromic subsequent's length
        def longest_palindromic_subseq(s):
            n = len(s)
            dp = [[0]*n for _ in range(n)]

            for i in range(n):
                dp[i][i] = 1  # single characters are palindromes

            for length in range(2, n+1):
                for i in range(n - length + 1):
                    j = i + length - 1
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])

            return dp[0][n-1]
        #find the length of the given string
        n = len(s)
        #find the length of longest palindromic subsequent of given string
        x = longest_palindromic_subseq(s)
        #acaluculate how many steps to do the given string to make palindrom
        return n-x
