class Solution:
    def findLucky(self, arr: list[int]) -> int:
        # Step 1: Count the frequency of each number.
        # Since arr[i] is between 1 and 500, we can use an array for frequency counting.
        # Initialize an array of size 501 with all zeros.
        # freq_map[x] will store the frequency of number x.
        freq_map = [0] * 501 
        
        for num in arr:
            freq_map[num] += 1
            
        # Step 2 & 3: Iterate from the largest possible number downwards
        # to find the largest lucky integer.
        # Start from 500 down to 1.
        for i in range(500, 0, -1):
            # Check if the number `i` has a frequency equal to its value `i`.
            if freq_map[i] == i:
                return i # Found the largest lucky integer, return it immediately.
                
        # Step 4: If no lucky integer is found after checking all numbers, return -1.
        return -1