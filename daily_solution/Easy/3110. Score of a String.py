class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_values = [ord(char) for char in s]
        result = 0
        for i in range(len(ascii_values)-1):
            result += abs(ascii_values[i]-ascii_values[i+1])
        return result
