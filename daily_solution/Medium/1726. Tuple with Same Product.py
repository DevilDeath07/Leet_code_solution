                            #python3

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        product_counts = {}  # Store counts of each product

        for i in range(n):
            for j in range(i + 1, n):  # Avoid duplicates (a,b) and (b,a) initially
                product = nums[i] * nums[j]
                product_counts[product] = product_counts.get(product, 0) + 1

        for product, freq in product_counts.items():
             count += freq * (freq - 1)

        return count * 4 
