class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            # If nums[mid] is greater than its right neighbor,
            # then a peak must exist in the left half (including mid).
            # This is because if nums[mid] > nums[mid+1], and nums[mid+1]
            # keeps decreasing, mid is a peak. If nums[mid+1] starts increasing
            # again, then there must be a peak to its right.
            # But since nums[mid] > nums[mid+1], we know that the peak cannot be
            # to the right of mid+1 if the sequence continues to decrease.
            # The peak could be mid itself or to its left.
            if nums[mid] > nums[mid + 1]:
                right = mid
            # If nums[mid] is less than its right neighbor,
            # then a peak must exist in the right half (excluding mid).
            # This is because the sequence is increasing towards the right,
            # so a peak must be further to the right.
            else:
                left = mid + 1
        
        # When left == right, we have found a peak element.
        return left