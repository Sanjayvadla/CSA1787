#tic tac toe game
l=[[0]*3 for _ in range(3)]



def check(m,i,j):
    l1=[]
    l2=[]
    d1=[]
    d2=[]
    for k in range(3):
        for l in range(3):
            if(k==i and m[k][l]==m[i][j]):
                l1.append('0')
            elif(l==j and m[k][j]==m[i][j]):
                l2.append('0')
    for k in range(3):
        for l in range(3):
            if(i==j):
                if(k==l and m[k][l]==m[i][j]):
                    d1.append('0')
            elif(i+j==2):
                if(k+j==2 and m[k][l]==m[i][j]):
                    d2.append('0')
    if(len(l1)==3 or len(l2)==3 or len(d1)==3 or len(d2)==3):
        return 1
    else:
        return 0

def play1():
    r=1
    print("Enter the first player place to print X : ")
    i=int(input("Enter the row number : "))
    j=int(input("Enter the column number : "))
    if(l[i][j]!=0):
        print("Already entered this position please re enter the numbers")
    else:
        l[i][j]='x'
        for c in l:
            print(c)

        n=check(l,i,j)
        if(n==1):
            print("player 1 is win")
            
        else:
            for q in range(3):
                for w in range(3):
                    if(l[q][w]!=0):
                        r=r*1
                    else:
                        r=r*0
            if(r==1):
                print("match is draw")
            else:
                play2()

def play2():
    print("Enter the second player place to print o : ")
    i=int(input("Enter the row number : "))
    j=int(input("Enter the column number :"))
    r=1
    if(l[i][j]!=0):
        print("Already entered this position please re enter the numbers")
    else:
        l[i][j]='o'
        for c in l:
            print(c)

        n=check(l,i,j)
        if(n==1):
            print("player 2 is win")
            h=1
        else:
            for q in range(3):
                for w in range(3):
                    if(l[q][w]!=0):
                        r=r*1
                    else:
                        r=r*0
            if(r==1):
                print("match is draw")
                h=1
            else:
                play1()

play1()
