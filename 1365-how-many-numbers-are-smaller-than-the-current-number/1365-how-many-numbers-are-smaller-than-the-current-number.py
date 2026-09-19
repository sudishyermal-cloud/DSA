class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        
        
        b=[]
        for i in nums:
            count=0
            for j in nums:
                if j<i:
                    count+=1
            b.append(count)
        return b 
        