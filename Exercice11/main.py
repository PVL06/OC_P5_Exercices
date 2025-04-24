
class BankAccount:
    def __init__(self, account_holder: str, balance: float) -> None:
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            print("impossible !!!")
        else:
            self.balance -= amount

    def display_balance(self):
        print(f"balance: {self.balance}\n")


bank = BankAccount("john", 1000)
print("dépot de 50")
bank.deposit(50)
bank.display_balance()

print("Retrait de 1051")
bank.withdraw(1051)
bank.display_balance()

print("Retrait de 100")
bank.withdraw(100)
bank.display_balance()
