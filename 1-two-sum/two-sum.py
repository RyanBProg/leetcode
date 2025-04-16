class Solution(object):
    def twoSum(self, nums, target):
        numberMap = {}

        for i in range(len(nums)):
            val = target - nums[i]
            if val in numberMap:
                return [numberMap[val], i]

            numberMap[nums[i]] = i