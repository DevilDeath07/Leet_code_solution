def is_self_dividing(number):
    for digit in str(number):
        if digit == '0' or number % int(digit) != 0:
            return False
    return True
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [nums for nums in range(left,right+1) if is_self_dividing(nums)]
