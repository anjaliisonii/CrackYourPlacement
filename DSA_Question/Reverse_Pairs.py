class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """c=0
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i]>2*nums[j]:
                    c+=1
        return c"""
        #this is using the merge sort and we have to do the two fuction for the merege and merge sort fuctions 
        def merge_sort(nums,left,right):
            count=0
            if left<right:
                mid=(left+right)//2
                count+=merge_sort(nums,left,mid)
                count+=merge_sort(nums,mid+1,right)
                count+=merge(nums,left,mid,right)
            return count
        def merge(nums,left,mid,right):
            count=0
            exhaust=mid+1
            for i in range (left,mid+1):
                while exhaust<=right and nums[i]>2*nums[exhaust] :
                    exhaust+=1
                count+=(exhaust-(mid+1))
            i=left
            j=mid+1
            temp=[]
            while i<=mid and j<=right:
                if nums[i]<=nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
            while i<=mid:
                temp.append(nums[i])
                i+=1
            while j<=right:
                temp.append(nums[j])
                j+=1
            for i in range (left,right+1):
                nums[i]=temp[i-left]
            return count


        n=len(nums)
        return merge_sort(nums,0,n-1)