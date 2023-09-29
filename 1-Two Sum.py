# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# -------------------------------------------
class Solution(object):
    def twoSum(self, nums, target):
        a = 0
        for num in nums:
            a+=1
            if target - num in nums[a:]:
                print(nums[a:])
                nums[a-1] = ':)'
                b = nums.index(target - num)
                print(target - num)
                a1 = [a-1, b]
                return a1
            else:
                continue
# -------------------------------------------
# Runtime 279 ms
# Beats 55.48%

# Memory 13.9 MB
# Beats 98.10%
