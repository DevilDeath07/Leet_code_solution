class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Step 1: Sort citations in descending order
        citations.sort(reverse=True)
        
        # Step 2: Iterate and find the maximum h
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
            else:
                break
        return h
