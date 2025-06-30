class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        if nums[left] <= nums[right]:
            return nums[left]

        while left <= right:
            mid = (left + right) // 2

            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1