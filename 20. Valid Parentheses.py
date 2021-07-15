class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ele in s:
            if ele == '(' or ele == '{' or ele == '[':
                stack.append(ele)
            else:
                if len(stack) ==0: # only ) or ] or }
                    return False
                if ele == ')' and stack.pop() != '(':
                    return False
                if ele == ']' and stack.pop() != '[':
                    return False
                if ele == '}' and stack.pop() != '{':
                    return False

        return len(stack) == 0 
