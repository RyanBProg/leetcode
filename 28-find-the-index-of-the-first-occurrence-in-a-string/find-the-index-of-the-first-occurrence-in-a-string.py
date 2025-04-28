class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            matching = True

            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    matching = False
                    break

            if matching:
                return i

        return -1