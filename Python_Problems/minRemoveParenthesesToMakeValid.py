class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_lst = list(s)
        stack = []

        for i, char in enumerate(s_lst):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    s_lst[i] = ''

        while stack:
            s_lst[stack.pop()] = ''

        return ''.join(s_lst)
