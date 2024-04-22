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
    str1="\n".join([str(i) for i in account['transactions']])
    try:
        a=open("trans2.txt","x")
        a.write("Initial Balance: ")
        a.write(str(bal))
        a.write("\n")
        a.write(str1)
        a.write("\n")
        a.write('Remaining Balance: $')
        a.write(str(account['balance']))
        a.write("\n")
        a.close()
        return account['transactions']
    except FileExistsError:
        a=open("trans2.txt","w")
        a.write("Initial Balance: ")
        a.write(str(bal))
        a.write("\n")
        a.write(str1)
        a.write("\n")
        a.write('Remaining Balance: $')
        a.write(str(account['balance']))
        a.write("\n")
        a.close()
        return account['transactions']
        

# Create an account dictionary
account = {
    'balance': 1000,
    'transactions': []
}
bal='$'+str(account['balance'])
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