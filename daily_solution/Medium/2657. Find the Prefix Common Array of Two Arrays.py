class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result=[0]*len(A)
        for i in range(len(A)):
            c=A[:i+1]
            d=B[:i+1]
            result[i]=compare1(c,d)
        return result

def compare1(A,B):
    m=len(A)
    count=0
    for j in range(m):
        for k in range(m):
            if A[j]==B[k]:
                count+=1
                break
            else:
                continue
    return count
