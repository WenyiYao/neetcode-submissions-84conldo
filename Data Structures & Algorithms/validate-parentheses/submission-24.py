class Solution:
    def isValid(self, s: str) -> bool:
        closedBracket = {")":"(", "]":"[", "}":"{"}
        stack = []
        for c in s:
            if stack and c in closedBracket:
                if closedBracket[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        
        return True if not stack else False

        