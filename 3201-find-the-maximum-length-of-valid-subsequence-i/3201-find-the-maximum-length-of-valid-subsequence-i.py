class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Case 1: All elements have the same parity.
        # This results in (same_parity + same_parity) % 2 == 0 for all adjacent sums.
        count_even_only = 0
        count_odd_only = 0
        for num in nums:
            if num % 2 == 0:
                count_even_only += 1
            else:
                count_odd_only += 1

        # Case 2: Elements alternate parity.
        # This results in (different_parity + different_parity) % 2 == 1 for all adjacent sums.
        # We use dynamic programming to find the longest alternating subsequence.
        # dp_alt_odd_ending: longest alternating subsequence found so far that ends with an odd number.
        # dp_alt_even_ending: longest alternating subsequence found so far that ends with an even number.
        
        # Initialize with 0. A single number can start a subsequence of length 1, 
        # which is handled by max(1, ...).
        dp_alt_odd_ending = 0
        dp_alt_even_ending = 0

        for num in nums:
            if num % 2 == 0:  # Current number is even
                # If we are extending an alternating sequence with an even number, 
                # the previous number in that sequence must have been odd.
                # Or, this even number can start a new sequence of length 1.
                dp_alt_even_ending = max(1, dp_alt_odd_ending + 1)
            else:  # Current number is odd
                # If we are extending an alternating sequence with an odd number, 
                # the previous number in that sequence must have been even.
                # Or, this odd number can start a new sequence of length 1.
                dp_alt_odd_ending = max(1, dp_alt_even_ending + 1)
        
        # The overall maximum length will be the maximum among:
        # 1. The longest subsequence of only even numbers.
        # 2. The longest subsequence of only odd numbers.
        # 3. The longest alternating subsequence (either ending in odd or even).
        
        return max(count_even_only, count_odd_only, dp_alt_odd_ending, dp_alt_even_ending)