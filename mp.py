class a:
    flag1=0
    flag2=0
    def p(self,e):
        if e==1:
            print(n, "is not a prime number")
            return 0
        elif e>1:
           for i in range(2,e):
               if (e%i)==0:
                   print(e,"is not a prime number")
                   return 0
               else:
                   print(e,"is a prime number")
                   return 1
        else:
           print(e,"is not a prime number")
           return 0
        
        
    def mp(self,n):
        flag1=self.p(n)
        t=n
        r=0
        m=0
        while n!=0:
            r=n%10
            m=(m*10)+r
            n=n//10
        flag2=self.p(m)
        if flag1==1 and flag2==1:
            print(t,"is Magical prime number")
        else:
            print(t,"is not a magical prime number")
x=a()
z=int(input("enter a number:"))
x.mp(z)


  
            
        