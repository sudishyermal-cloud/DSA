class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        x=0
        for i in range(n):
            a=start+2*i
            nums.append(a)
        for j in nums:
            
            x=x^j
        return x  