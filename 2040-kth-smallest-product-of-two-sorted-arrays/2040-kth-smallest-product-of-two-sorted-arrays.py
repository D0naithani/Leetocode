import bisect

class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        
        # This helper function counts the number of products less than or equal to 'val'
        def count_less_than_or_equal(val):
            count = 0
            for num in nums1:
                if num == 0:
                    # If num is 0, any product with a non-zero number is 0.
                    # If val is non-negative, any product with 0 is <= val.
                    if val >= 0:
                        count += len(nums2)
                elif num > 0:
                    # For a positive number, we need to count elements in nums2
                    # that are <= val / num.
                    # Since nums2 is sorted, we can use binary search (bisect_right).
                    count += bisect.bisect_right(nums2, val / num)
                else:  # num < 0
                    # For a negative number, we need to count elements in nums2
                    # that are >= val / num.
                    # This means we need to find the number of elements from the end of nums2.
                    # We can use binary search (bisect_left).
                    # The range of valid numbers would be from index 0 to the index of the first
                    # number > val / num.
                    
                    # Example: num = -4, val = -8, val/num = 2. We need products <= -8.
                    # nums2 = [2, 4]. We need 2 * j <= -8, j <= -2. No elements.
                    # num = -4, val = -10, val/num = 2.5. We need 2 * j <= -10, j <= -2.5. No elements.
                    # num = -4, val = -16, val/num = 4. We need 2 * j <= -16, j <= -4. No elements.
                    # It's a bit tricky due to integer division and signs.
                    # Let's count elements in nums2 where the product is > val.
                    # Then total pairs - count_greater_than = count_less_than_or_equal.
                    # A more direct approach: find the number of elements `j` in `nums2` such that `num * j <= val`.
                    # Since `num` is negative, this is equivalent to `j >= val / num`.
                    # So we need to count elements in `nums2` from `bisect_left(nums2, val / num)` onwards.
                    
                    # bisect_left returns the insertion point for `val / num` to maintain order.
                    # The elements from that index onwards are >= val / num.
                    insertion_point = bisect.bisect_left(nums2, val / num)
                    count += len(nums2) - insertion_point
            return count

        # Set the search range for binary search
        # Minimum possible product: min(min(nums1) * max(nums2), max(nums1) * min(nums2))
        # Maximum possible product: max(min(nums1) * min(nums2), max(nums1) * max(nums2))
        # A wider range is safer to avoid edge cases.
        low = -10**10  # A sufficiently small number
        high = 10**10  # A sufficiently large number
        ans = high

        while low <= high:
            mid = (low + high) // 2
            
            # Count how many products are less than or equal to mid
            count = count_less_than_or_equal(mid)

            if count >= k:
                # If the count is >= k, it means the kth smallest product is at most mid.
                # So we can potentially find a smaller product.
                ans = mid
                high = mid - 1
            else:
                # If the count is < k, mid is too small. We need a larger product.
                low = mid + 1

        return ans