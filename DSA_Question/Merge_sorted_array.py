class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
    
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return 
        j=len(nums1)-1
        while n>0 and m>0:
            if nums2[n-1]>=nums1[m-1]:
                nums1[j]=nums2[n-1]
                n-=1
            else:
                nums1[j]=nums1[m-1]
                m-=1
            j-=1
            print(nums1)
        while n>0:
            nums1[j]=nums2[n-1]
            n-=1
            j-=1
        #Inplace sorting Brute force
        # for c in range(m,m+n):
        #     if(nums1[c] == 0):
        #         nums1[c] = nums2[c-m]
        # nums1.sort()

        #Another solution
        
        
        