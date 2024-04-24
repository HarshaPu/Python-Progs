a=(input("enter the numbers:").split(','))
for i in range(0,len(a)):
    a[i]=int(a[i],2)
for j in a:
    if(j%5==0):
        print(j)