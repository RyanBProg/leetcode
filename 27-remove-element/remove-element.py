class Solution(object):
    def removeElement(self, nums, val):
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
            else:
                count += 1

        return count