class Solution(object):
    def plusOne(self, digits):
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                carry = 1
                digits[i] = 0
            else:
                digits[i] += 1
                carry = 0
                break

        if carry == 1:
            digits[0] = 1
            digits.append(0)

        return digits