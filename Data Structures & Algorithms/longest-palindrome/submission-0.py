class Solution:
    def longestPalindrome(self, s: str) -> int:

        n = len(s)
        my_set = set()
        length = 0 

        for i in range (0,n):
            if s[i] in my_set:
                length += 2
                my_set.remove(s[i])
            else:
                my_set.add(s[i])

        if len(my_set) > 0:
            length += 1

        return length 
        