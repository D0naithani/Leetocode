class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        max_ending_here = nums[0]
        min_ending_here = nums[0]
        max_product_so_far = nums[0]
        
        for i in range(1, len(nums)):
            current_num = nums[i]
            
            temp_max = max(current_num, max_ending_here * current_num, min_ending_here * current_num)
            
            min_ending_here = min(current_num, max_ending_here * current_num, min_ending_here * current_num)
            
            max_ending_here = temp_max
            
            max_product_so_far = max(max_product_so_far, max_ending_here)
            
        return max_product_so_far