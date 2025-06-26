class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        """
        Finds the length of the longest subsequence of s that makes up a binary
        number less than or equal to k.
        """
        
        # We greedily build the longest subsequence from right to left,
        # which corresponds to building the binary number from least significant bit to most significant bit.
        
        n = len(s)
        subsequence_value = 0
        length = 0
        
        # power_of_2 represents the place value (2^0, 2^1, 2^2, ...) of the bit
        # we are currently considering adding to our subsequence.
        power_of_2 = 1
        
        # Iterate through the string from right to left
        for i in range(n - 1, -1, -1):
            char = s[i]
            
            if char == '0':
                # We can always include a '0' as it doesn't change the value.
                # It just increases the length of the subsequence.
                length += 1
                
            elif char == '1':
                # If the current bit is '1', we check if adding it to our subsequence
                # would exceed the limit k.
                # The value this '1' would add is power_of_2.
                
                if subsequence_value + power_of_2 <= k:
                    subsequence_value += power_of_2
                    length += 1
            
            # Update the power of 2 for the next position to the left.
            # We need to be careful not to overflow if we were in C++/Java.
            # In Python, integers handle arbitrary size, so we can check against k.
            if power_of_2 <= k:
                power_of_2 *= 2
            
        return length
        