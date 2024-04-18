class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        dicts = {")": "(", "]": "[", "}": "{"}
        
        for p in s:
            if p in dicts.keys():
                if stack == [] or dicts[p] != stack.pop():
                    return False
            else:
                stack.append(p)
                
        return not stack