import numpy as np
class Solution:
    def addDigits(self, num: int) -> int:
        
        if num < 10:
            return num
        else:
            digits = [int(digit) for digit in str(num)]
            num1 = int(np.sum(digits))
            return self.addDigits(num1)


        
