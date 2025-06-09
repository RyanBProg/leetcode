class Solution(object):
    def lengthOfLastWord(self, s):
        start_index = None
        end_index = None

        for i in range(len(s) - 1, -1, -1):
            if end_index != None and start_index != None:
                break

            if end_index == None:
                if s[i] != " ":
                    end_index = i
            else:
                if s[i] == " ":
                    start_index = i
        
        if end_index is None:
            return 0

        if start_index is None:
            return end_index + 1
            
        return end_index - start_index