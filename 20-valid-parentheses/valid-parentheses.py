class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)   # push opening bracket
            elif ch in ")}]":
                if not stack:   # no opening bracket
                    return False
                top = stack.pop()
                if (ch == ")" and top != "(") or \
                (ch == "}" and top != "{") or \
                (ch == "]" and top != "["):
                    return False
        return not stack  # balanced if stack empty




        