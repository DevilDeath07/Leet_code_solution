class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()  # Remove non-alphanumeric and lowercase
        return cleaned_string == cleaned_string[::-1]  # Check palindrome 
