# Power Of Numbers
# https://practice.geeksforgeeks.org/problems/power-of-numbers-1587115620/1

#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        #Your code here
        if R==1:
            return N
        ans=self.power(N,R//2)
        if R%2==0:
            return (ans*ans)%(10**9+7)
        else:
            return (N*ans*ans)%(10**9+7)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends