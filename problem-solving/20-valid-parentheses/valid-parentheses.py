class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        stack = []
        ind = 0
        openset = ('(', '[', '{')
        while ind < len(s):
            i = s[ind]
            if i in openset:
                stack.append(i)
            else:
                if stack and ((i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') or (i == '}' and stack[-1] == '{')):
                    stack.pop()
                else: return False
            ind += 1
        
        if not stack: 
            return True
        else:
            return False

        