class Solution:
    def isValid(self, word: str) -> bool:
        # Condition 1: Minimum length of 3 characters
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        for char in word:
            if '0' <= char <= '9':
                # It's a digit, allowed
                continue
            elif 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                # It's an English letter
                if char in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
            else:
                # It's an invalid character ('@', '#', '$', etc.)
                return False
        
        # Condition 3 & 4: At least one vowel and at least one consonant
        return has_vowel and has_consonant