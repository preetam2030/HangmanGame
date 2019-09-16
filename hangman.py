import numpy as np
import sys
filename="words1.txt"
wrdlist=np.loadtxt(filename,delimiter='\n',dtype=str)
#print(wrdlist)
l=[]
n=int(input("Enter no of letters 1-13 "))
lives=int(input("Enter no of lives "))
#lives<n ?????
for i in range(wrdlist.size):
    if len(wrdlist[i])==n:
        l.append(wrdlist[i])
word=l[np.random.randint(0,len(l))]
def game(wrd,liv):
    gss="*"*len(wrd)
    guess=[]
    used=[]
    flag=0
    while (gss!=wrd and liv>0):
        g=input("Guess a letter ")
        if(g.isalpha()==False):
            print("Expected an alphabet")
            print()
            continue
        flag=0
        if g in used:
            print("Already guessed this")
            print()
            continue
        used.append(g)
        for i in range(len(wrd)):
            guess=list(gss)
            if (g.casefold()==wrd[i].casefold()):
                guess[i]=g
                flag=1
                gss="".join(guess)
        if flag==0:
            liv=liv-1
            print("Wrong guess "+gss)
            print("Lives left "+str(liv))
            print("Used words are: "+", ".join(used))
            print()
        else:
            print("Correct guess "+gss)
            print("Lives left "+str(liv))
            print("Used words are: "+", ".join(used))
            print()
            
    if liv==0:
        print("All lives are lost")
        print(word)
    if gss==wrd:
        print("Congratulation, You Won")
game(word,lives)
