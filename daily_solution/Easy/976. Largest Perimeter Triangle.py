class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        def is_valid_triangle(a, b, c):
            return b+c > a
        for i in range(len(nums)-2):
            a,b,c = nums[i],nums[i+1],nums[i+2]
            if is_valid_triangle(a,b,c):
                return a+b+c
        return 0
