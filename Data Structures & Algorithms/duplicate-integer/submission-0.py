class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:


        n = len(nums)
        hash ={}

        for i in range(0,n):
            if nums[i] in hash:
                return True
            
            hash[nums[i]] = i 
        
        return False
        