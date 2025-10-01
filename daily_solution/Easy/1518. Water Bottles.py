class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drinkedcount = numBottles 
        bal_empty = numBottles 
        while bal_empty>=numExchange: 
            new = bal_empty // numExchange
            drinkedcount +=new 
            bal_empty = bal_empty - (new*numExchange)+new 
        return drinkedcount
