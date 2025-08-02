class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and len(token) > 1):
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b) if a * b > 0 else -(-a // b))

        return stack.pop()
        