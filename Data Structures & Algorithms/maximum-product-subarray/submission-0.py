class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        lp = 1
        rp = 1
        ans = nums[0]

        for i in range (0,n):
            if lp == 0:
                lp = 1
            if rp == 0:
                rp =1

            lp = lp * nums[i]

            rp = rp * nums[n-1-i]

            ans = max (ans, lp, rp)

        return ans 
        