class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        for i in range(0,len(s),k):
            result +=[s[i:i+k]]
        last_value = len(result)-1

        if len(result[last_value])==k:
            return result
        else:
            while len(result[last_value])!=k:
                result[last_value]+=fill
            return result
