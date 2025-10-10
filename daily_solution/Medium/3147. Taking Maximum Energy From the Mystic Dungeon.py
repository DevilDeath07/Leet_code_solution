class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        prefix = [0] * n
        prefix[0] = energy[0]
        for i in range(n -1, -1, -1):
            if i + k < n:
                prefix[i] = energy[i] + prefix[i + k]
            else:
                prefix[i] = energy[i]  
        return max(prefix)          
