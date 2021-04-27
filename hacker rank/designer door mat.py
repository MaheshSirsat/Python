#https://www.hackerrank.com/challenges/designer-door-mat/problem

a,b=(int(x) for x in input().split())
temp=3
for i in range(1,a+1):
    print("-"*(int((b-temp)/2)),end="")
    print(".|."*((i*2)-1),end="")
    print("-"*(int((b-temp)/2)))
    temp=temp+6
    t=int((b-temp)/2)
    if t==0:
        break
#MIDDLE LINE
print("-"*(int((b-7)/2)),end="")
print("WELCOME",end="")
print("-"*(int((b-7)/2)))
temp=3
for i in range(a,0,-1):
    print("-"*temp,end="")
    print(".|."*int((b-(temp*2))/3),end="")
    print("-"*temp)
    if ((temp*2)+3)==b:
        break
    temp=temp+3