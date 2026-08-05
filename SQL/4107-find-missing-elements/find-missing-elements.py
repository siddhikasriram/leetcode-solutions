class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        a = min(nums)
        b = max(nums)

        for i in range(a,b+1):
            if i not in nums: 
                ans.append(i)
        return ans