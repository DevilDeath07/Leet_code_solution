class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #convert binary into integer number 
        temp1 = int(a, 2)
        temp2 = int(b,2)
        #add the two convertetd numbers
        result = temp1 + temp2
        #convert integer into binary number
        ans = format(result, 'b')
        return ans
