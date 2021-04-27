#https://www.hackerrank.com/challenges/no-idea/problem

a=input().split()
n,m=map(int,a)
arr=input().split()
array=list(map(int,arr))
a=input().split()
A=set(map(int,a))
b=input().split()
B=set(map(int,b))
hap=0
for i in array:
    if i in A:
        hap=hap+1
    elif i in B:
        hap=hap-1
    else:
        hap=hap+0
print(hap)
