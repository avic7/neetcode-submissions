class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        L = 0
        H = n - 1

        while L <= H:
            M = (L+H) // 2

            if nums[M] == target:
                return M

            if nums[M] <= nums[H]:
                if nums[M] <= target <= nums[H]:
                    L = M + 1 
                else:
                    H = M - 1

            else: 
                if nums[L] <= target <= nums[M]:
                    H = M - 1
                else:
                    L = M + 1 

        return -1