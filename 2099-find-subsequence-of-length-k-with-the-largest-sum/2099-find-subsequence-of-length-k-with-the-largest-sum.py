class Solution:
    def maxSubsequence(self, nums, k):
        """
        Finds a subsequence of length k with the largest sum.

        Args:
            nums: An integer array.
            k: The desired length of the subsequence.

        Returns:
            A subsequence of nums of length k with the largest sum.
        """
        # 1. Create pairs of (value, original_index)
        indexed_nums = []
        for i in range(len(nums)):
            indexed_nums.append((nums[i], i))

        # 2. Sort by value in descending order
        #    If values are equal, the order of original indices doesn't matter for sum,
        #    but sorting by value is enough to get the largest numbers.
        indexed_nums.sort(key=lambda x: x[0], reverse=True)

        # 3. Select the top k elements
        top_k_elements = indexed_nums[:k]

        # 4. Sort by original_index in ascending order to preserve original order
        top_k_elements.sort(key=lambda x: x[1])

        # 5. Extract the values to form the subsequence
        result_subsequence = [x[0] for x in top_k_elements]

        return result_subsequence

# The _driver() function would typically be part of the testing harness
# and would create an instance of the Solution class like this:
# ret = Solution().maxSubsequence(param_1, param_2)