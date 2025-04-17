class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False

        divNum = 1
        while x >= 10 * divNum:
            divNum *= 10

        while x:
            if x % 10 != x // divNum: return False

            x = (x % divNum) // 10
            divNum = divNum // 100

        return True

        