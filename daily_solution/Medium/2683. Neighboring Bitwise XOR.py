class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n=len(derived)
        original=[0]*n
        original[0]=0
        for i in range(n-1):
            original[i+1]=original[i]^derived[i]
        original[0] = original[n - 1] ^ derived[n - 1]

        check=[0]*n
        for i in range(0,n):
            if i==(n-1):
                check[i]=original[i]^original[0]
            else:
                check[i]=original[i]^original[i+1]
        return check == derived
