class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s += char.lower()
                

        def func(string, left, right):
            if left >= right:
                return True
            
            if string[left] != string[right]:
                return False 
            
            return func(string, left + 1, right - 1)

        return func(clean_s, 0, len(clean_s) - 1)
