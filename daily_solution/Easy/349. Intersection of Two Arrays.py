class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [] #result the array of their intersection it must be unique
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                #check nums1 element and nums2 elemtnt same and not in result list then append in the result list
                if nums1[i] == nums2[j] and nums1[i] not in result:
                    result.append(nums1[i])#store the element in the result list
        #return the result list
        return result
