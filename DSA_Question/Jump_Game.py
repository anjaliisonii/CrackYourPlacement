class Solution:
    def canJump(self,nums: List[int]) -> bool:
        max1=0
        for i in range (len(nums)):
            if i>max1:
                return False
            max1=max(max1,i+nums[i])
        return True
        '''
        #greedy
        n=len(nums)
        l=n-1
        for i in range (n-2,-1,-1):
            if i+nums[i]>=l:
                l=i
        if l==0:
            return True
        else:
            return False
        '''
        #dp
        n=len(nums)
        track=[False for i in range (n)]
        track[n-1]=True
        for i in range (len(nums)-2,-1,-1):
            for j in range (i+1,i+nums[i]+1):
                if track[j]==True:
                    track[i]=True
                    break
        if track[0]==True:
            return True
        else:
            return False
                
    '''
    #exponential t.c
        pos=0
        return self.Jump(nums,pos)
    def Jump(self,nums,pos):
        if pos==len(nums)-1:
                return True
        max_jump=min(pos+nums[pos],len(nums)-1)
        for j in range (pos+1,max_jump+1):
            if self.Jump(nums,j):
                return True
        return False
    '''
        
         