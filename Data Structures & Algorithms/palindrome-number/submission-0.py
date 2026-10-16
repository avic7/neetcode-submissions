class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        original = x
        reverse_num = 0 

        while original > 0 : 
            last_digit = original % 10 

            reverse_num = (reverse_num * 10) + last_digit

            original = original // 10 

        
        if reverse_num == x:
            return True
        else:
            return False
        