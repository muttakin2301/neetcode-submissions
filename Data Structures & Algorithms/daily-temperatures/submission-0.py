class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        stack = []
        minday = [0] * size

        for i in range(size):
            if not stack:
                stack.append(i)
                continue

            while stack and temperatures[stack[-1]] < temperatures [i]:
                minday[stack[-1]] = i - stack[-1]
                stack.pop()
                
            stack.append(i)

        return minday
