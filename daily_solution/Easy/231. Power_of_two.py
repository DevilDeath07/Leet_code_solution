class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #check the number less then or greater than because the power will always positive then return false
        if n <= 0:
            return False
        #use math.log2() function is used to check the what the power of n might be
        log_result = math.log2(n)
        #check for whole number. 
        #they have log2(n) value is wholenumber then they will be the power of 2; otherwise it is not to the power of 2.
        return log_result.is_integer()
        
