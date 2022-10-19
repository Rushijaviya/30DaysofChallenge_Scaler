# Simple Text Editor
# https://www.hackerrank.com/challenges/simple-text-editor/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=""
record=[""]
for _ in range(n):
    temp=input()
    if temp[0]=='1':
        s+=temp[2:]
        record.append(s)
    elif temp[0]=='2':
        s=s[:-int(temp[2:])]
        record.append(s)
    elif temp[0]=='3':
        print(s[int(temp[2:])-1])
    else:
        record.pop()
        s=record[-1]