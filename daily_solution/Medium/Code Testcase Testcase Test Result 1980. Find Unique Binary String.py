class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        binary = []
        for i in range(2**n):  
            temp = format(i, f'0{n}b')  
            binary.append(temp)
        for ele in binary:
            if ele not in nums:
                return ele
