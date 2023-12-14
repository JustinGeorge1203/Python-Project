class Banking_System:
    def __init__(self):
        self.log_in = False
        self.username=None
        self.user_database = [{"account_no":1122,"username":"Ryan","password":"1234","balance":0},{"account_no":2211,"username":"Lia","password":"1234","balance":500}]
    def login(self,username,password):
        for user in self.user_database:
            if user["username"]==username and user["password"]==password:
                self.log_in=True
                self.username=username
                print("Login Successful!")
                break
        else:
             print("Invalid Account Number.Login Failed!")
    def deposit(self,amount):
        if self.log_in:
            for user in self.user_database:
                if user["username"]==self.username:
                    user["balance"]+=amount
                    print(f"Deposit of ${amount} successful.Current balance is ${user["balance"]}")
                    break
    def withdraw(self,amount):
        if self.log_in:
            for user in self.user_database:
                if user["username"]==self.username:
                    if user["balance"]>=amount:
                        user["balance"]-=amount
                        print(f"Withdrawal of ${amount} is successful.Current balance is ${user["balance"]}")
                    else:
                        print("Insufficient funds!")
                        break
    def balance(self):
        if self.log_in:
            for user in self.user_database:
                if user["username"]==self.username:
                    print(f"Current balance for {self.username}=${user["balance"]}")
                    break

bank=Banking_System()
print("Welcome to the Banking System")
username_input=input("Enter username: ")
password_input=input("Enter password: ")
bank.login(username_input,password_input)

while True:
    if not bank.log_in:
        print("Please login to proceed!")
        break
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")
    choice=input("Enter your choice(1-4):")
    if choice=="1":
        if bank.login:
            deposit_amount=float(input("Enter amount to deposit: $"))
            bank.deposit(deposit_amount)
        else:
            print("Please login to proceed!")
    elif choice=="2":
        if bank.login:
            withdraw_amount=float(input("Enter amount to withdraw: $"))
            bank.withdraw(withdraw_amount)
        else:
            print("Please login to proceed!")
    elif choice=="3":
        bank.balance()
    elif choice=="4":
        print("Thank you for banking with us.")
        break
    else:
        print("Invalid Choice")
