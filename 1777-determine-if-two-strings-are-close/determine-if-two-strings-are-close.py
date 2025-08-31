class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1)!=len(word2):
            return False
        h1,h2={},{}
        i,j=0,0
        while i<len(word1) and j<len(word2):
            h1[word1[i]]=h1.get(word1[i],0)+1
            i+=1
            h2[word2[j]]=h2.get(word2[j],0)+1
            j+=1
        if set(h1.keys())!=set(h2.keys()):
            return False

        cs1=sorted(h1.values())
        cs2=sorted(h2.values())
        return cs1==cs2