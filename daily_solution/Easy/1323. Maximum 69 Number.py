class Solution:
    def maximum69Number (self, num: int) -> int:
        if num >10000:
            return 
        return int(str(num).replace('6', '9', 1))
        
