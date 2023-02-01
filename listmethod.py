#list methods add,append,delete,extend
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[1,2,3,4]
print("add method ")
print(l1+l2)
print("append")
for i in l1:
    l2.append(i)
print(l2)
l2=[5,6,7,8]
print("delete : ")
l1.remove(4)
print("After removing 4 in l1",l1)

print()

print("extend : ")
l3.extend(l2)
print(l3)
