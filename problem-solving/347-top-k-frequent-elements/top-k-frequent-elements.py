class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        d = {} 
        i =0 

        for n in nums: 
            if n in d:
                d[n] += 1 
            else:
                d[n] = 1
        
        d_list = list(d.items())

        d_list.sort(key = lambda x:x[1], reverse = True)

        for i in range(k):
            result.append(d_list[i][0])

        return result
     