class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count1=0
        count2=0
        for i in range(len(nums)):
            
            if nums[i]==1:
                
                count1=count1+1
            else:
                
                count1=0
            count2=max(count1,count2)
        return count2