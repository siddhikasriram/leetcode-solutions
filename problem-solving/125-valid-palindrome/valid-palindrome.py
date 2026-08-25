class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].isalnum() == False:
                i += 1
            elif s[j].isalnum() == False:
                j -= 1
            
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False

    
        return True


        

        

        