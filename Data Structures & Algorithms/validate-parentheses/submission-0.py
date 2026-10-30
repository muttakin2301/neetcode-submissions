class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if len(stack) == 0:
                stack.append(p)
                continue

            last = stack.pop()

            if((last == "(" and p == ")") or (last == "{" and p == "}") or (last == "[" and p == "]")):
                continue

            stack.append(last)
            stack.append(p)

        if len(stack) == 0:
            return True
        return False


