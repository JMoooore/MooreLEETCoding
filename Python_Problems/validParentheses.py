# Test Cases
# '' -> True
# '[({})] -> True
# '[{' -> False
# '[{(})]' -> False
# '[{}()]' -> True
# '})' -> False

class Solution:
    def isValid(self, s: str) -> bool:
        # do we only have brackets parentheses etc? -> Yes
        # how do we treat an empty string -> True
        # initialize stack as an empty array
        stack = []

        # iterate through all the charactersLoL
        for char in s:
            # if the character is a left paren add it to the stack
            if char in ['[', '(', '{']:
                stack.append(char)
            # if the character is right paren
            else:
                # if correct right paren pop the left paren
                if len(stack) > 0:
                    if stack[-1] == '[' and char == ']' or stack[-1] == '(' and char == ')' or stack[-1] == '{' and char == '}':
                        stack.pop()
                    else:
                        return False
                # if wrong right paren return False
                else:
                    return False
        # if stack is empty
            # return true
        # if stack is not
            # return false
        return len(stack) == 0