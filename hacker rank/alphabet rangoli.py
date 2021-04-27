#https://www.hackerrank.com/challenges/alphabet-rangoli/problem

a=int(input())
for i in range(a,0,-1):
    print("-"*((i*2)-2),end="")
    for ii in range(a,i,-1):
        print(chr(96+ii),end="-")
    for iii in range(i,a+1):
        if iii==a:
            print(chr(96+iii),end="")
        else:
            print(chr(96+iii),end="-")
    print("-"*((i*2)-2))
for j in range(2,a+1,1):
    print("-"*((j*2)-2),end="")
    for jj in range(a,j-1,-1):
        print(chr(96+jj),end="-")
    for jjj in range(j+1,a+1):
        if jjj!=a:
         print(chr(96+jjj),end="-")
        else:
         print(chr(96+jjj),end="-")
    print("-"*((j*2)-3))