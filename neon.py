class a:
    def neon(self,n):
        s=n*n
        t=n
        r=0
        m=0
        while s!=0:
            r=s%10
            m=m+r
            s=s//10
        if n==m:
            print(n," is a neon number")
        else:
            print(n," is not a neon number")
x=a()
z=int(input("enter a number:"))
x.neon(z)