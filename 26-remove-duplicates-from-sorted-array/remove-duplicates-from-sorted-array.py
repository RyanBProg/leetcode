class Solution(object):
    def removeDuplicates(self, nums):
        unique_count = 0
        i = 0
        total_loop = len(nums)

        while i < total_loop:
            if i == total_loop - 1:
                unique_count += 1
                i += 1
            elif nums[i] == nums[i + 1]:
                nums.pop(i)
                # nums.append(nums[i])
                total_loop -= 1
            else:
                unique_count += 1
                i += 1

        return unique_count
        