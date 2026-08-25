


class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for ind, n in enumerate(nums):
            ans = target-n
            if ans in d:
                return [d[ans], ind]
            else:
                d[n] = ind

