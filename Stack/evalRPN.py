import operator
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []

        ops = {
            '+' : lambda x, y: x + y,
            '-' : lambda x, y: y - x,
            '*' : lambda x, y: x * y,
            '/' : lambda x, y: int(operator.truediv(y, x)) 
        }

        for idx, item in enumerate(tokens):
            if item not in ops:
                stack.append(item)
            else:
                if len(stack) >= 2:
                    res = ops[item](int(stack[-1]), int(stack[-2]))
                    stack.pop()
                    stack.pop()
                    stack.append(res)
            
        return int(stack[-1])
