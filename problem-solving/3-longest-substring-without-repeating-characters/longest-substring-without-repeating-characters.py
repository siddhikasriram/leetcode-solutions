class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = 0
        j =0
        m =0
        st = set()

        while j < len(s):
            if s[j] not in st:
                st.add(s[j])
                j += 1
                m = max(m, j-i)
            else: 
                st.remove(s[i])
                i += 1
        return m
