class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1)!=len(word2):
            return False
        h1=Counter(word1)
        h2=Counter(word2)

        return set(h1.keys())==set(h2.keys()) and sorted(h1.values())==sorted(h2.values())