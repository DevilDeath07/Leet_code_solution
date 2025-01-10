#using some built in package and functions

from collection import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        req = Counter()
        for words in words2:
            cur = Counter(words)
            for ch in cur:
                req[ch] = max(req[ch], cur[ch])
        
        result = []
        for words in words1:
            cur = Counter(words)
            if all(cur[ch] >= req[ch] for ch in req):
                result.append(words)
        
        return result   
