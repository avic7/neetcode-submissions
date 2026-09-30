class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 
        
        maap = {}

        for ch in s:
            maap[ch] = maap.get(ch,0)+1 
        
        for ch in t:
            if ch not in maap:
                return False
            else:
                if maap[ch]==0:
                    return False 
                else:
                    maap[ch] -= 1
        
        return True
        