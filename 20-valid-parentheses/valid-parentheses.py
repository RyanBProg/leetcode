class Solution(object):
    def isValid(self, s):
        brackets = {
            "{": "}",
            "[": "]",
            "(": ")",
        }

        openStack = []

        for char in s:
            if char in brackets:
                openStack.append(char)
            else:
                if not openStack:
                    return False
                else:
                    lastOpen = openStack.pop()
                    if char != brackets[lastOpen]:
                        return False

        return len(openStack) == 0