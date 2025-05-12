from typing import List
from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # Count occurrences of each digit
        digit_count = Counter(digits)
        
        result = set()
        
        # Iterate over valid three-digit numbers (100-999)
        for num in range(100, 1000, 2):  # Only even numbers
            num_str = str(num)
            temp_count = Counter(map(int, num_str))  # Count digits in the number
            
            # Check if we have enough digits in the original list
            if all(temp_count[d] <= digit_count[d] for d in temp_count):
                result.add(num)
        
        return sorted(result)  # Sorted list of valid even numbers
