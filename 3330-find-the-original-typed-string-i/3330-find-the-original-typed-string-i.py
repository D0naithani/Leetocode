class Solution:
    def possibleStringCount(self, word: str) -> int:
        total_possible_strings = 1
        
        i = 0
        n = len(word)
        while i < n:
            current_char = word[i]
            run_length = 0
            j = i
            while j < n and word[j] == current_char:
                run_length += 1
                j += 1
            
            if run_length > 1:
                total_possible_strings += (run_length - 1)
            
            i = j
            
        return total_possible_strings