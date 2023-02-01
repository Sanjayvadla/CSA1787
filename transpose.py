try:
    r=int(input("Enter the number of rows : "))
    c=int(input("Enter the number of columns : "))
    l=[]
    temp=0
    l1=[]
    for i in range(r):
        m=list(map(int,input().split(",")))
        if(len(m)==c):
            l.append(m)
        else:
            print("enter elements that is equal to number of columns ")
    for i in range(r):
        for j in range(c):
            if(i+j not in l1):
                l1.append(i+j)
                temp=l[i][j]
                l[i][j]=l[j][i]
                l[j][i]=temp            
    for i in l:
        print(i)
        print()
except ValueError:
    print("Enter the correct data type ")
