class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_no = account_number
        self.holders_name = holder_name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -=amount
        else:
            print("Umesota Bro!!!")
    def display_balance(self):
        print(f"account_number:{self.account_no}")
        print(f"holder_name{self.holders_name}")
        print(f"balance{self.balance}")
my_account = BankAccount("1234567890", "Teanna", 10000)
my_account.display_balance()
my_account.deposit(5000)
my_account.display_balance()
my_account.withdraw(10000000)
my_account.display_balance()