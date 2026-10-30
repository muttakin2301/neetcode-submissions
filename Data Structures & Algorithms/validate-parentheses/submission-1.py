class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for p in s:
            if len(stack) == 0:
                stack.append(p)
                continue

            if p in mapping and mapping[p] != stack.pop():
                return False
            elif p not in mapping:
                stack.append(p)

        if len(stack) == 0:
            return True
        return False


