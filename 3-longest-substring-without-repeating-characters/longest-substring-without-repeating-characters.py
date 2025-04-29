class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        chars = set()
        highest = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            highest = max(highest, r - l + 1)
            
        return highest