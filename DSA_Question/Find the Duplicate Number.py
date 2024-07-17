class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #1 Uing the extra space:
        # dict1={}
        # for i in nums:
        #     if i not in dict1:
        #         dict1[i]=1
        #     else:
        #         dict1[i]+=1
        # for i,v in dict1.items():
        #     if v>=2:
        #         return i
        # using the change in array:
        # nums.sort()
        # for i in range (1,len(nums)):
        #     if nums[i-1]==nums[i]:
        #         return nums[i]
        #using the constant space:using the slow and fast pointer floyd's Cycle
        slow=0
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


        
