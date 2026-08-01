class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        n = x 
        out = 0

        while n >= 1:
            reminder = n % 10
            out = reminder + out * 10
            n = n/10
        return out == x











        #solution:

        # x = str(x)
        # if x == x[::-1]:
        #     return True
        # else:
        #     return False

        