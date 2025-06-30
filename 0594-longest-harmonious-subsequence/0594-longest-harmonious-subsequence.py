from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        counts = Counter(nums)
        max_length = 0

        for num in counts:
            if num + 1 in counts:
                current_length = counts[num] + counts[num + 1]
                max_length = max(max_length, current_length)
        
        return max_length