import numpy as np
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # Convert list to array
        temp = np.array(digits)
        #convert array of digits into number
        stemp = int(''.join(map(str, temp)))

        #add one in the array
        stemp +=1

        #convert the array into list
        result = list(map(int, str(stemp)))
        return result
