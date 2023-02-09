class Solution:	
    #Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, N, K):
		# code here
        l=N-1
        n=0
        b=[]
        while True:
            if n>l:
                a=arr[n:l+1]
                b+=a[::-1]
                break
            else:
                a=arr[n:n+K]
                b+=a[::-1]
                n=n+K
        for i in range(0,N):
            arr[i]=b[i]

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1
if __name__=="__main__":
    main()
