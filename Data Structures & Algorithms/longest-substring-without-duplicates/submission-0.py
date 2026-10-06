class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        my_dict = {}
        L = 0
        R = 0
        maxi = 0 

        while R < n:
            if s[R] in my_dict:
                L = max (L, my_dict[s[R]]+1)

            maxi = max ( maxi, R-L+1)
            my_dict[s[R]] = R
            R += 1

        return maxi 
        