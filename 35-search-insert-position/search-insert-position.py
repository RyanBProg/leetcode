class Solution(object):
    def searchInsert(self, nums, target):
        if nums[0] == target:
            return 0
        if nums[-1] == target:
            return len(nums) - 1

        a = 0
        b = len(nums) - 1

        while a <= b:
            mid = (a + b) // 2
                
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                b = mid - 1
            elif target > nums[mid]:
                a = mid + 1

        return a
