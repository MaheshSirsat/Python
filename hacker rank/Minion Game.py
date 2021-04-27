#Question---> https://www.hackerrank.com/challenges/the-minion-game/problem

#Solution:
def minion_game(string):
    l=len(string)
    c,v=0,0
    for ss in range(l):
        if string[ss] in "AEIOU":
            v=v+(l-ss)
        else:
            c=c+(l-ss)
    #print(c,v)
    if c>v:
        print("Stuart {}".format(c))
    if c<v:
       print("Kevin {}".format(v))
    if c==v:
        print("Draw")