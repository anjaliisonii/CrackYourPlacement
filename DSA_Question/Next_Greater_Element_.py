class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #We have to search for the nums1 of num2 of the elements
        def search(key,ind,nums2):
            nums=-1
            for j in nums2[ind+1:]:
                if (j>key):
                    nums=j
                    break
            return nums
        ans=[]
        for i in range (len(nums1)):
            ind=nums2.index(nums1[i])
            yes=search(nums1[i],ind,nums2)
            # print(yes)
            ans.append(yes)
        return ans
        