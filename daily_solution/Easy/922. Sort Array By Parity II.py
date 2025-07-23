class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_numbers = [num for num in nums if num % 2 == 0]
        odd_numbers = [num for num in nums if num % 2 != 0]

        # Alternate even and odd values
        result = []
        for even, odd in zip(even_numbers, odd_numbers):
            result.extend([even, odd])
        return result
        
