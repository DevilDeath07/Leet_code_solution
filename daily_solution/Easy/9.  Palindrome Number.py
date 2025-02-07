class Solution:
    def isPalindrome(self, x: int) -> bool:
        #using string to find the value is palindrome or not
        res = str(x) == str(x)[::-1]
        if res:#the value is palindrome return true
            return True
        else:#otherwise return False
            return False
