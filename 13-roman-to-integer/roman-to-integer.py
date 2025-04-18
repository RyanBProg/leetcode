class Solution(object):
    def romanToInt(self, s):
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,

        }

        answer = 0

        for i in range(len(s) - 1, -1, -1):
            prevChar = s[i + 1] if i + 1 < len(s) else None
            char = s[i]

            if char == "I":
                if prevChar == "V" or prevChar == "X":
                    answer -= 1
                    continue
            if char == "X":
                if prevChar == "L" or prevChar == "C":
                    answer -= 10
                    continue
            if char == "C":
                if prevChar == "D" or prevChar == "M":
                    answer -= 100
                    continue
            if symbols[char]: answer += symbols[char]

        return answer