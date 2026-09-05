class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
    
        for c in tokens:
            if c in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if c == "+":
                    stack.append(operand1+operand2)
                elif c =="-":
                    stack.append(operand1-operand2)
                elif c =="*":
                    stack.append(operand1*operand2)
                else:
                    sign = -1 if operand1 * operand2 < 0 else 1
                    stack.append(sign * (abs(operand1) // abs(operand2)))
            else:
                stack.append(int(c))
        
        return stack[-1]
