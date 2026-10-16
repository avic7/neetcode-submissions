class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0 

        for i in range (0,n):
            left , right = i,i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

            left,right = i,i+1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        return res
        