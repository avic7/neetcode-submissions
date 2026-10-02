class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        left = 0
        right = n-1
        max_water = 0 

        while left < right: 
            ch = min(heights[left], heights[right])
            cw = right - left 
            area = ch * cw

            max_water = max(max_water,area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water 
        