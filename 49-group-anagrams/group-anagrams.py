class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        results = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for l in word: 
                key[ord(l) - ord('a')] +=1
            results[tuple(key)].append(word)

        return results.values()

        
                

        
        