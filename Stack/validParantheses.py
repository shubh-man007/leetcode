class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        hash_s = {")" : "(", "]" : "[", "}" : "{"}

        for item in s:
            if item not in hash_s:
                stack.append(item)
            else:
                if len(stack) > 0 and stack[-1] == hash_s[item]:
                    stack.pop()
                else:
                    stack.append(item)
                
        if len(stack) == 0:
            return True
        else:
            return False    
