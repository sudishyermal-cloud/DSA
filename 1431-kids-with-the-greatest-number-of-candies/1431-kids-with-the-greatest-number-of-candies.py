class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        n=max(candies)
        b=[]
        c=[]
        for i in candies:
            b.append(i + extraCandies)
        for i in b:
            if i>=n:
                i=True
                c.append(i)
            else:
                i=False
                c.append(i)    
        return c