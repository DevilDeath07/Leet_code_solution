from collections import Counter
import numpy as np
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        def all_elements_greater(array, number):
            return all(element > number for element in array)
        n = len(nums)
        maximum = np.max(nums)
            
        result = []
        for i in range(n):
            for j in range(i+1,n):
                temp = nums[i]+nums[j]
                result.append(temp)
        if all_elements_greater(result, maximum):
            count = Counter(result)   
            for i in result:
                if len(count)==3:
                    return "scalene"
                elif len(count)==2:
                    return "isosceles"
                elif len(count)==1:
                    return "equilateral"
        else:
            return "none"
          
