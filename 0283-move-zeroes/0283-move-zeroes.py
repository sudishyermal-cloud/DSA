class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=[]
        b=[]
        for i in nums:
            if i!=0:
                b.append(i)
            elif i==0:
                c.append(i)

        nums[:]=b+c
        return nums
        