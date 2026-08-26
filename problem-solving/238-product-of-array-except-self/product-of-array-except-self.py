class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        preSum = []
        sufSum = [1]*len(nums)
        ans = []
        #calc prefix sums
        for i in range(len(nums)): 
            if i == 0:
                preSum.append(1)
            else:
                preSum.append(nums[i-1] * preSum[i-1])
        
        #calc suf sums
        for i in range(len(nums)-2, -1, -1):
   
            sufSum[i] = nums[i+1] * sufSum[i+1]
        print(preSum, sufSum)
        for i in range(len(nums)):
            ans.append(preSum[i] * sufSum[i])
        return ans




        
        
        