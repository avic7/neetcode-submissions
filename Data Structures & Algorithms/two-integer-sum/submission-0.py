class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        hash = {}

        for i in range (0, n):
            diff = target - nums[i]
            if diff in hash:
                return [hash[diff],i]

            hash[nums[i]] = i 

        