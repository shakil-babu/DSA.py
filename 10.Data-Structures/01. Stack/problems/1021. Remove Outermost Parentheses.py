class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res = ""
        for item in s:
            if item == "(":
                if len(stack) > 0:
                    res += item
                stack.append(item)

            else:
                stack.pop()
                if len(stack) > 0:
                    res += item

        return res
