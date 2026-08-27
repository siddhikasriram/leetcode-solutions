class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        d = {}
        lookup = {}
        for i in s1:
            if i in lookup:
                lookup[i] += 1
            else:
                lookup[i] = 1
            
        left = 0
        right = len(s1) - 1
        i = 0
        while i < len(s1):

            if s2[i] in d:
                d[s2[i]] += 1
            else:
                d[s2[i]] = 1
            i += 1
        
        

        while right < len(s2):
            print(d)
            if lookup != d:
                right = right + 1

                if right < len(s2):
                    if s2[right] in d:
                        d[s2[right]] += 1
                    else:
                        d[s2[right]] = 1
                else:
                    return False

                d[s2[left]] -= 1
                if d[s2[left]] == 0:
                    del d[s2[left]]
            else:
                return True
            left += 1


        return False
        
                


        

        