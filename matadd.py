try:
    r1=int(input("Enter the number of rows in first matrix : "))
    c1=int(input("Enter the number of columns in first matrix : "))
    r2=int(input("Enter the number of rows in second matrix : "))
    c2=int(input("Enter the number of columns in second matrix : "))
    
    l=[]
    l1=[]
    l2=[]
    print("mat1 : ")
    for i in range(r1):
        m=list(map(int,input('').split(',')))
        if(len(m)==c1):
            l.append(m)
        else:
            print("enter the elements in column size : ")
    print(l)
    print("mat2 : ")
    for i in range(r2):
        m=list(map(int,input('').split(',')))
        if(len(m)==c2):
            l1.append(m)
        else:
            print("enter the elements in column size : ")
    print(l1)
    print("Addition of the two matrix is :")
    result = [[l[i][j] + l1[i][j]  for j in range(len(l[0]))] for i in range(len(l))]
    print(result)
except ValueError:
    print("Enter the correct datatype: ")
