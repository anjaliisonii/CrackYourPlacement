class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Brute force
        # max1=0
        # for i in range (len(height)):
        #     for j in range (i+1,len(height)):
        #         max1=max(max1,(j-i)*min(height[i],height[j]))
        # return max1
        #Two pointer
        i=0
        j=len(height)-1
        max1=0
        while i<j:
            length=min(height[i],height[j])
            bredth=j-i
            max1=max(max1,length*bredth)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1

        return max1