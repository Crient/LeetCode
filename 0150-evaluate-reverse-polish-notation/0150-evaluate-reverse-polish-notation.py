class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            if s == "+":
                right = stack.pop()
                left = stack.pop()
                stack.append(left + right)

            elif s == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)

            elif s == "*":
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)

            elif s == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))

            else:
                stack.append(int(s))

        return stack[0]