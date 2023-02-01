k=input("enter the string : ")
punc='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
r=1
s=''
l=[]
for i in k:
    l.append(i)
for i in k:
    for j in punc:
        if(i==j):
            r=r*0
    if(r!=0):
        s=s+i
        r=1
    else:
        r=1
print(s)
