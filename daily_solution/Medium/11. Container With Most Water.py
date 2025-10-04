class Solution:
    def maxArea(self, height: List[int]) -> int:
        #use the two pointer approach
        left = 0
        right = len(height) - 1
        max_width = 0

        while left < right:
            breadth = right - left
            length = min(height[left],height[right])
            max_width = max(max_width, (breadth * length))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_width
