class Solution:
    
    def runningSum(self, nums: list[int]) -> list[int]:
        b=[]
        t=0

        for i in range(len(nums)):
            t=t+nums[i]
            b.append(t)
        return b    


        