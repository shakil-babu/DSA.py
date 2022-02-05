class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        stack = []
        for item in s:
            if item == "(":
                stack.append(item)
            elif item == ")":
                ans = max(ans, len(stack))
                stack.pop()

        return ans
