s=input("enter : ")
l=[]
l2=[]
a=0
l1=['+','-','*','/']
for i in s:
    if(i not in l1):
        l.append(i)
    else:
        l2.append(i)
#converting the float value
for i in range(len(l)):
    if(l[i]=='.'):
        l[i-1]=l[i-1]+'.'+l[i+1]
        l[i-1]=float(l[i-1])
        l[i]=0
        l[i+1]=0
#removing 0
for i in l:
    if i==0 :
        l.remove(i)
for i in range(len(l)):
    l[i]=float(l[i])

#division
for i in range(0,len(l2)-1):
    if(l2[i]=='/'):
        l[i]=l[i]/l[i+1]
        l[i+1]=0
        l2[i]=' '
#multipication
for i in range(len(l2)):
    if(l2[i]=="*"):
        l[i]=l[i]*l[i+1]
        l[i+1]=0
        l2[i]=' '
a=l[0]
for i in range(len(l2)):
    if(l2[i]=='+'):
        a=l[i+1]+a
    elif(l2[i]=='-'):
        a=a-l[i+1]
print(a)


