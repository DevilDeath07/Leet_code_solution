class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        dp0 = [[0]*(one+1) for _ in range(zero+1)]
        dp1 = [[0]*(one+1) for _ in range(zero+1)]
        
        # base cases: arrays consisting only of zeros or only of ones
        for t in range(1, min(limit, zero)+1):
            dp0[t][0] = 1
        for t in range(1, min(limit, one)+1):
            dp1[0][t] = 1
        
        for i in range(zero+1):
            for j in range(one+1):
                # extend with zeros
                for t in range(1, min(limit, i)+1):
                    dp0[i][j] = (dp0[i][j] + dp1[i-t][j]) % MOD
                # extend with ones
                for t in range(1, min(limit, j)+1):
                    dp1[i][j] = (dp1[i][j] + dp0[i][j-t]) % MOD
        
        return (dp0[zero][one] + dp1[zero][one]) % MOD


----------------------------------------(or)--------------------------------------------
it passes 666 test case but not completely pass all the test cases

brute force approach:  (itertools approach)

import itertools

MOD = 10**9 + 7

zero = 3
one = 3
limit = 2
length = zero + one

# Generate all binary strings with exactly `zero` zeros and `one` ones
binary = []
for ones_positions in itertools.combinations(range(length), one):
    word = ''.join('1' if i in ones_positions else '0' for i in range(length))
    binary.append(word)

# Check stability: no run of identical digits longer than `limit`
def is_stable(word, limit):
    run = 1
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            run += 1
            if run > limit:
                return False
        else:
            run = 1
    return True

# Count stable arrays modulo 1e9+7
count = 0
for word in binary:
    if is_stable(word, limit):
        count = (count + 1) % MOD

print("Number of stable arrays:", count)
