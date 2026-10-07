class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)
        my_dict = {}
        left = 0
        max_f = 0
        max_l = 0

        for right in range (len(s)):
            my_dict[s[right]] = my_dict.get(s[right],0) +1
            

            max_f = max(max_f, my_dict[s[right]])
            window_size = right - left + 1

            if window_size - max_f > k:
                my_dict[s[left]] -= 1
                left += 1

            max_l = max(max_l, right - left+1)

        return max_l
        