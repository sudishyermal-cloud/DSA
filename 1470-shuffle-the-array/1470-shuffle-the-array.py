class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        b=[]
        if len(nums)==2*n:
            for i in range(n):
                b.append(nums[i])
                b.append(nums[i+n])
            return b    
             
