class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s: str) -> str: 
            return ''.join('1' if ch == '0' else '0' for ch in s)

        s = "0"
        for i in range(2,n+1):
            s = s +"1"+invert(s)[::-1]
        return s[k-1]
