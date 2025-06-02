class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        char_count = {}

        # Count characters in s
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1

        # Subtract counts based on t
        for c in t:
            if c not in char_count:
                return False
            char_count[c] -= 1
            if char_count[c] < 0:
                return False

        return True
