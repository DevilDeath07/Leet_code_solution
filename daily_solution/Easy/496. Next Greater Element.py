from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = []  # Fixing incorrect initialization
        for i in range(len(nums1)):
            found = False  # Flag to indicate if we found nums1[i] in nums2
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:  # Correcting comparison
                    found = True
                    # Check for next greater element
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums1[i]:
                            temp.append(nums2[k])
                            break
                    else:
                        temp.append(-1)
                    break
            if not found:
                temp.append(-1)  # Handle cases where nums1[i] is not found in nums2

        return temp
