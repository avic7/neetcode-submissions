class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_dict = {}
        for ch in t:
            t_dict[ch] = t_dict.get(ch, 0) + 1

        window_dict = {}    
        left = 0 
        have = 0
        need = len(t_dict)

        res = [-1, -1]
        min_l = float("inf")

        for right in range(len(s)):
            window_dict[s[right]] = window_dict.get(s[right], 0) + 1

            if s[right] in t_dict and window_dict[s[right]] == t_dict[s[right]]:
                have += 1

            while have == need:
                window_size = right - left + 1

                if window_size < min_l:
                    min_l = window_size
                    res = [left, right]

                window_dict[s[left]] -= 1

               
                if s[left] in t_dict and window_dict[s[left]] < t_dict[s[left]]:
                    have -= 1

                left += 1

        
        left_idx, right_idx = res
        return s[left_idx : right_idx + 1] if min_l != float("inf") else ""