class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        Evaluates an arithmetic expression in Reverse Polish Notation.

        Args:
            tokens: An array of strings representing the RPN expression.

        Returns:
            An integer that represents the value of the expression.
        """
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in operators:
                # If the token is an operand (a number), push it onto the stack.
                stack.append(int(token))
            else:
                # If the token is an operator, pop the two operands.
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    # Integer division truncates toward zero.
                    # Python's int() function handles this correctly for both positive and negative numbers.
                    result = int(operand1 / operand2)

                # Push the result back onto the stack.
                stack.append(result)

        # The final result is the only element left on the stack.
        return stack.pop()

# Example Usage:
tokens1 = ["2", "1", "+", "3", "*"]
solution = Solution()
print(f"Input: {tokens1}\nOutput: {solution.evalRPN(tokens1)}")

tokens2 = ["4", "13", "5", "/", "+"]
print(f"Input: {tokens2}\nOutput: {solution.evalRPN(tokens2)}")

tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(f"Input: {tokens3}\nOutput: {solution.evalRPN(tokens3)}")

tokens4 = ["18"]
print(f"Input: {tokens4}\nOutput: {solution.evalRPN(tokens4)}")