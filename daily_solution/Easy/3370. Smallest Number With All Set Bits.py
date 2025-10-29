class Solution:
    def smallestNumber(self, n: int) -> int:
        binary_string = bin(n)[2:]
        ll_ones_binary = '1' * len(binary_string)
        decimal_number = int(ll_ones_binary, 2)
        return decimal_number
