'''Given an array A[ ] of N elements.
In one operation, you can select any subarray of length 2 and multiply all elements of that subarray by -1. You can do any number of operations (possibly zero).
Your task is to maximize the sum of all elements of all subarrays of A[ ].'''
class Solution:
    def maxSum(self, N, A): 
        #code here
        ans=0
        ct=0
        mx=-1
        ok=0
        for i in range(N):
            x=(i+1)*(N-i)
            x*=A[i]
            if A[i]==0:
                ok=1
            if A[i]<0:
                ct+=1
            if mx==-1:
                mx=abs(x)
            else:
                mx=min(mx,abs(x))
            ans+=abs(x)
        if ct%2==0 or ok:
            return ans
        return ans-2*mx
