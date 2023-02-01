#LIST OPERATIONS
l=[]
l.append([1,2,3])
l.append([4,5,6])
l1=[7,8,9]
l2=[11,12,13]

#nested list
print("Nested list : ")
print(l)
#length
print("length : ")
print(len(l))
#concate
print("concate : ")
print(l1+l2)
#iteration
print("iteration : ")
for i in l2:
    print(i,end=' ')
#membership operator
print("membership operator : ")
print("3 in l1",3 in l1)
print("7 in l1",7 in l1)

#indexing
print("Index : ")
print("l1.index(9) : ",l1.index(9))

#slicing
print("slicing")
print("l1[0:2] : ",l1[0:2])
