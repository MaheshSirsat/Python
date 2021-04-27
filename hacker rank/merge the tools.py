#https://www.hackerrank.com/challenges/merge-the-tools/problem

a=input()
length=len(a)
b=int(input())
limit=int(length/b)
j=[]
l=[]
for i in range(0,length,b):
    j.append(a[i:i+b:])
p=""
for item in j:
    p=""
    for k in item:
       if k in p:
           pass
       else:
           print(k,end="")
           p=p+k
    print()

