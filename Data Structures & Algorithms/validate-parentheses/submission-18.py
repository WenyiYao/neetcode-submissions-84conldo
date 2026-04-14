class Solution:
    def isValid(self, s: str) -> bool:
        closedBracket = {"(":")", "[":"]", "{":"}"}
        stack = []
        for c in s:
            if c in closedBracket:
                stack.append(c)
            else:
                if stack:
                    
                    if c == closedBracket[stack[-1]]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        return True if not stack else False

        