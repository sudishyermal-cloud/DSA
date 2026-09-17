class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n=0
        s=0
        for i in accounts:
            n=sum(i)
            if n>s:
                s=n
        return s    