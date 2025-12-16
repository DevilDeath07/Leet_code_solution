class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return n

        total = n      # all single-element periods
        streak = 1     # current descent streak length

        for i in range(1, n):
            if prices[i-1] - prices[i] == 1:
                streak += 1
            else:
                streak = 1
            total += (streak - 1)

        return total
----------------------------------(or)------------------------------------

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        #initial how much length of the given list is one part so we initialize the length in default orher will calculate and add after
        sdp = len(prices)
        if(sdp<2):
            return sdp

        #find sub array
        def all_subarrays(arr):
            n = len(arr)
            subarrays = []
            for start in range(n):
                for end in range(start + 2, n + 1):
                    subarrays.append(arr[start:end])
            return subarrays
        subarray = all_subarrays(prices)   
        #create loop for the price on each day is lower than the price on the preceding day by exactly 1.
        sub_count = 0
        for sarr in subarray:
            # Calculate differences
            temp = [sarr[i] - sarr[i + 1] for i in range(len(sarr) - 1)]
            if all(x == 1 for x in temp):
                sub_count +=1
        return sdp+sub_count
