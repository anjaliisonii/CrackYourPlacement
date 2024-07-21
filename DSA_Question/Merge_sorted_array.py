class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Inplace sorting Brute force
        for c in range(m,m+n):
            if(nums1[c] == 0):
                nums1[c] = nums2[c-m]
        nums1.sort()

        #Another solution
        
        
        