class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if i == ')' and top == "(" or i == '}' and top == "{" or i == ']' and top == "[":
                    continue
                else:
                    return False
        if len(stack) == 0:
            return False
        return True