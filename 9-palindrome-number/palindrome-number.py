class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        num = x
        newNum = 0

        while x > 0:
            newNum = newNum * 10 + x % 10
            x //= 10

        return newNum == num

        