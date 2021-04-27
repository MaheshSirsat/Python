#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

a=int(input())
b=set(int(x) for x in input().split())
c=list(b)
c.sort()
print(c[-2])
