class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_score = 0
        
        # Determine which pair gives more points
        # Prioritize removing the pair that gives more points
        if x >= y:
            first_pair = "ab"
            first_points = x
            second_pair = "ba"
            second_points = y
        else:
            first_pair = "ba"
            first_points = y
            second_pair = "ab"
            second_points = x

        # Function to process the string for a given pair
        def remove_pair(current_s: str, pair: str, points: int) -> (str, int):
            stack = []
            score = 0
            for char in current_s:
                if stack and stack[-1] == pair[0] and char == pair[1]:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return "".join(stack), score

        # First pass: remove the higher-scoring pair
        remaining_s_after_first_pass, score_first_pass = remove_pair(s, first_pair, first_points)
        total_score += score_first_pass

        # Second pass: remove the lower-scoring pair from the remaining string
        _, score_second_pass = remove_pair(remaining_s_after_first_pass, second_pair, second_points)
        total_score += score_second_pass

        return total_score