class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        nums.sort()
        
        powers_of_2 = [1] * n
        for i in range(1, n):
            powers_of_2[i] = (powers_of_2[i - 1] * 2) % MOD
            
        left = 0
        right = n - 1
        count = 0
        
        while left <= right:
            if nums[left] + nums[right] <= target:
                count = (count + powers_of_2[right - left]) % MOD
                left += 1
            else:
                right -= 1
                
        return count