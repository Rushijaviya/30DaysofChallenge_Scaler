# Xor Palindrome
# https://www.codechef.com/submit/XOR_PAL

# cook your dish here
t=int(input())
while t:
    t-=1
    n=int(input())
    l=input()
    start=0
    end=n-1
    count=0
    while start<end:
        if l[start]!=l[end]:
            count+=1
        start+=1
        end-=1
    x=(count+1)//2 if count%2 else count//2
    print(x)