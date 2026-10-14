class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums)
        L = 0 
        H = n - 1 
        mini = float("inf")

        while L <= H :
            M = (L+H) // 2

            if nums[M] <= nums[H]:
                mini = min(mini, nums[M])
                H = M - 1
            else:
                mini = min(mini, nums[L])
                L = M + 1

        return mini
        