class Solution:
    def minimumLength(self, s: str) -> int:
        charmap=Counter(s)
        delete=0
        for i in charmap.values():
            if i%2==1:
                delete+=i-1
            else:
                delete+=i-2
        return len(s)-delete
