class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        intgr = 0
        operation = "+"

        for i in range(len(s)):
            char  = s[i]
            if char.isdigit():
                intgr = intgr*10 + int(char)
            
            if char in "+-/*" or i == len(s)-1:
                if operation == "+":
                    stack.append(intgr)
                elif operation == "-":
                    stack.append(-intgr)
                elif operation == "*":
                    stack.append(stack.pop()*intgr)
                elif operation == "/":
                    stack.append(int(stack.pop()/intgr))
                operation  = char
                intgr = 0
        
        return sum(stack)
        
        
