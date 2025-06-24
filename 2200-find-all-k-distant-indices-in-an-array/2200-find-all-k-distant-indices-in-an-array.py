class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        n = len(nums)
        k_distant_indices = []

        for i in range(n):
            is_k_distant = False
            for j in range(n):
                if nums[j] == key and abs(i - j) <= k:
                    is_k_distant = True
                    break  # Found a valid j for the current i, no need to check further
            if is_k_distant:
                k_distant_indices.append(i)

        return k_distant_indices