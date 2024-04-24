a=input("enter a string:")
c=0
c1=0
for i in a:
    if i.isdigit()==True:
        c+=1
    elif i.isalpha()==True:
        c1+=1
print('Letters:',c1)
print('Digits:',c)