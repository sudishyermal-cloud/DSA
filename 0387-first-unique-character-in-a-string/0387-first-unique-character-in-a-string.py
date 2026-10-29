class Solution:
    def firstUniqChar(self, s: str) -> int:
        l=[]
        for ch in s:
            l.append(ch)
        for i in l:
            if s.count(i)==1:
                return l.index(i)
                break
        return -1