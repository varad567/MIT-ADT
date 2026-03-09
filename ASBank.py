class BankAccount:
    
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Account No.:", self.acc_no)
        print("Amount Deposited:", amount)
        print("Updated Balance:", self.balance)
        print("----------------------------------")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Account No.:", self.acc_no)
            print("Amount Withdrawn:", amount)
            print("Updated Balance:", self.balance)
        print("----------------------------------")

    def check_balance(self):
        print("Account No.:", self.acc_no)
        print("Current Balance:", self.balance)
        print("----------------------------------")



acc1 = BankAccount("ABC0001", 50000)
acc1.deposit(5000)

acc2 = BankAccount("ABC0002", 10000)
acc2.withdraw(500)

acc3 = BankAccount("ABC0003", 1000000)
acc3.check_balance()
