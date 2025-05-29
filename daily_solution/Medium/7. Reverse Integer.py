class Solution:
    def reverse(self, x: int) -> int:
        temp = str(x)
        
        # Reverse digits and handle negative sign
        if temp[0] == "-":
            reversed_string = "-" + temp[:0:-1]  # Reverse everything except '-'
        else:
            reversed_string = temp[::-1]

        result = int(reversed_string)
        
        # Check 32-bit integer bounds
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result
