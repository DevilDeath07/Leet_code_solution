from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for word in strs:
            key = tuple(sorted(word))
            groups[key].append(word)
        
        return list(groups.values())
