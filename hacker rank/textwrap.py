#https://www.hackerrank.com/challenges/text-wrap/problem

a=input()
b=int(input())
bb=b
upp=bb
pre=0
list=[]
temp=""
for i in range(int(((len(a))/4)+1)):
    temp=a[pre:upp]
    list.append(temp)
    pre=upp
    upp=upp+b
for bomb in list:
    print(bomb)