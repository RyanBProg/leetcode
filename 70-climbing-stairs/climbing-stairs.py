class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n

        one, two = 2, 1
        for _ in range(3, n + 1):
            one, two = one + two, one
        return one


        