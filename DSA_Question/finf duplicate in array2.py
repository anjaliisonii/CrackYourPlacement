class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #fadduuuu approch using the negative flag of that number if finf duplicate
        ans =[]
        n=len(nums)
        for x in nums:
            x = abs(x)
            if nums[x-1]<0:
                ans.append(x)
            nums[x-1] *= -1
            # print(nums)
        return ans
        
        