class Solution(object):
    def lengthOfLongestSubstring(self, s):
        st = ""
        max_len = 0

        for i in s:
            if i not in st:
                st += i
                max_len = max(max_len, len(st))
            else:
                # remove characters from the start until duplicate is removed
                st = st[st.index(i)+1:] + i

        return max_len
