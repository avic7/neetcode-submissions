class Solution:
    def isPalindrome(self, s: str) -> bool:

        cs = ""
        for char in s:
            if char.isalnum():
                cs = cs + char.lower()

        
        n = len(cs)

        left = 0
        right = n-1

        while left < right:
            if cs[left] != cs[right]:
                return False 

            left = left +1
            right = right -1

        return True         