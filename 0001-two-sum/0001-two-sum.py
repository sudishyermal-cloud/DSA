class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d={}
        for i in range(len(nums)):
            if -10**9<= target <= 10**9 and -10**9<= nums[i] <= 10**9:
                need = target-nums[i]
                if need in d:
                    return [d[need], i]
                
                d[nums[i]]=i