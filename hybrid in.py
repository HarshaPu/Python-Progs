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
class b(a):
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
class c(a):
    def x(self,m):
        length=len(m)
        for i in range(length):
            for j in range(length):
                if i==j or i+j==length-1:
                    print(m[i],end=" ")
                else:
                    print(" ",end=" ")
            print()
class d(a):
    def rev(self,r):
        print(r[::-1])
class e(b,c):
    def bank(self):
        def withdraw(account, amount):
            if amount > account['balance']:
                print("Insufficient funds!")
        
            else:
                account['balance'] -= amount
                account['transactions'].append(f"Withdrawal: ${amount}")
                print(f"Withdrawal successful. Remaining balance: ${account['balance']}")
       

        def deposit(account, amount):
            account['balance'] += amount
            account['transactions'].append(f"Deposit: ${amount}")
            print(f"Deposit successful. Remaining balance: ${account['balance']}")

        def get_balance(account):
            return account['balance']

        def get_transaction_history(account):
        #str1="\n".join([str(i) for i in account['transactions']])
            '''a=open("trans106.txt","a")
            a.write("\n")
            a.write(str1)
            a.close()'''
            return account['transactions']

# Create an account dictionary
        account = {
            'balance': 1000,
            'transactions': []
        }

# Dictionary to map user choices to functions
        m=0
        e=input("enter your email:")
        p=input("enter your password:")
        p1="0123"
        e1="zealgaming4@gmail.com"

        if(e==e1) and (p==p1):
            choices = {
                '1': deposit,
                '2': withdraw,
                '3': get_balance,
                '4': get_transaction_history
            }

            while True:
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Transaction History")
                print("5. Exit")

                choice = input("Enter your choice: ")

                if choice == '5':
                    print("Exiting program.")
                    break

                if choice in choices:
                    if choice == '1':
                        amount = float(input("Enter amount: "))
                        choices[choice](account, amount)
            
                    elif choice == '2':
                        m=m+1
                        if m>5:
                            print("withdrawing limit reached")
                        else:
                            amount = float(input("Enter amount: "))
                            choices[choice](account, amount)
        
                    else:
                        print(choices[choice](account))
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid credentials")
      
obj=e()
obj1=d()
obj.mp(17)
obj.neon(9)
obj.x("harsha")
obj1.rev("harsha")
obj.bank()



  
            
        
