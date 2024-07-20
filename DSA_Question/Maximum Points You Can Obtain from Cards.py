class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n=len(cardPoints)-1
        first=[0]
        last=[0]
        for i in range (k):
            n1=first[-1]+cardPoints[i]
            first.append(n1)
        print(first)
        peeche=n-k
        for i in range (n,peeche,-1):
            n1=last[-1]+cardPoints[i]
            last.append(n1)
        print(last)
        max1=0
        for i in range (k+1):
            cs=first[i]+last[k-i]
            max1=max(max1,cs)
        return max1
        """"  l=0
        e=len(cardPoints)-1
        return self.solve(cardPoints,l,e,k)
    def solve(self,cardPoints,l,e,k):
        if k==0:
            return 0
        op1=cardPoints[l]+self.solve(cardPoints,l+1,e,k-1)
        op2=cardPoints[e]+self.solve(cardPoints,l,e-1,k-1)
        return max(op1,op2)"""
        
        