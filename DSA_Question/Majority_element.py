class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Brute force
        d1={}
        for i in range (len(nums)):
            if nums[i] not in d1:
                d1[nums[i]]=1
            else:
                d1[nums[i]]+=1
            if d1[nums[i]]>(len(nums)//2):
                return nums[i]

        #Another solution:Moore Voting Algorithm
        #he intuition behind the Moore's Voting Algorithm is based on the fact that if there is a majority element in an array, 
        # it will always remain in the lead, even after encountering other elements.
        count=0
        tot=0
        for i in nums:
            if count==0:
                tot=i
            if i==tot:
                count+=1
            else:
                count-=1
        return tot