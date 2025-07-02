MOD = 10**9 + 7

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        # Step 1: Group consecutive characters
        groups = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        # Total combinations (product of group sizes)
        ans = 1
        for o in groups:
            ans = ans * o % MOD

        # If number of groups is less than k, subtract invalid cases
        if len(groups) < k:
            f = [1] + [0] * (k - 1)
            g = [1] * k
            for group in groups:
                f_new = [0] * k
                for j in range(1, k):
                    f_new[j] = g[j - 1]
                    if j - group - 1 >= 0:
                        f_new[j] = (f_new[j] - g[j - group - 1]) % MOD
                g_new = [f_new[0]] + [0] * (k - 1)
                for j in range(1, k):
                    g_new[j] = (g_new[j - 1] + f_new[j]) % MOD
                f, g = f_new, g_new
            return (ans - g[k - 1]) % MOD

        return ans
