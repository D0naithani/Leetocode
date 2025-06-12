from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = 0
        n = len(nums)

        for i in range(n):
            current_diff = abs(nums[i] - nums[(i + 1) % n])
            if current_diff > max_diff:
                max_diff = current_diff

        return max_diff