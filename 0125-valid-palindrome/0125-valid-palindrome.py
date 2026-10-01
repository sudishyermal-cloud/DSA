class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        d = ''.join(char.lower() for char in s if char.isalnum())
        if d==d[::-1]:
            return True
        else:
            return False

