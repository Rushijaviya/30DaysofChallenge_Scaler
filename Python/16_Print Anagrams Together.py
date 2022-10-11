# Print Anagrams Together
# https://practice.geeksforgeeks.org/problems/print-anagrams-together/1

#User function Template for python3
# from collections import defaultdict
class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        d={}
        for word in words:
            x=sorted(word)
            x="".join(x)
            if x in d:
                d[x].append(word)
            else:
                d[x]=[word]
        ans=[]
        for i in d:
            ans.append(d[i])
        return ans
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends