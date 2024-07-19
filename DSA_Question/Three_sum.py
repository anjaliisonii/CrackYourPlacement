class Solution:
    def find_pairs(self,arr,left,target,result):
        right=len(arr)-1
        while(left<right):
            curr=arr[left]+arr[right]
            if curr==target:
                triplets=[]
                triplets.append(-target)
                triplets.append(arr[left])
                triplets.append(arr[right])
                result.append(triplets)
                
                left+=1
                right-=1
                #it remove the duplicacy like [-1,-2,-1,0,1,1,1] like this
                while(arr[left]==arr[left-1] and left<right):
                    left+=1
                while(arr[right]==arr[right+1] and left<right):
                    right-=1
            elif target>curr:
                left+=1
            else:
                right-=1
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range (len(nums)):
            target=-nums[i]
            #here we are skipping when the single number make the 0 like [-3,-3,-1,0] so -1 will be skiiped here
            if i>0 and nums[i]==nums[i-1]:
                continue
            self.find_pairs(nums,i+1,target,result)
        return result
                
            
            
                
            