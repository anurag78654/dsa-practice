# Pattern: Stack (evaluation)
# Intuition: push numbers; on operator, pop two operands, apply, push result

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        sol = []
        operator = "+-*/"
        for i in tokens:
            if i in operator:
                a, b = sol.pop(), sol.pop()
                if i == "+":
                    sol.append(b + a)
                elif i == "-":
                    sol.append(b - a)
                elif i == "*":
                    sol.append(b * a)
                elif i == "/":
                    sol.append(int(float(b) / a))
            else:
                sol.append(int(i))
        return sol[0]