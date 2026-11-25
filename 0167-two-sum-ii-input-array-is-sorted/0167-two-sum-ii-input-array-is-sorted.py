class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left=0
        right=len(numbers)-1
        while(left<right):
            c=numbers[left]+numbers[right]
            if c==target:
                return [left+1,right+1]
            elif c<target:
                left+=1
            else:
                right-=1

       