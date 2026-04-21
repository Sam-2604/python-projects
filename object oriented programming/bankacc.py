# write a BankAccount class that:

# __init__ takes owner (non-empty string) and balance (must be >= 0, default 0) — raise ValueError for violations
# Instance method deposit(amount) — amount must be positive, adds to balance
# Instance method withdraw(amount) — amount must be positive and not exceed balance, raises ValueError if either violated
# __str__ returns "[owner]'s account: $[balance]" formatted to 2 decimal places

# Then main():

# Create an account, deposit, withdraw, print at each step
# Attempt an overdraft and handle the error

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner}'s account: ${self.balance:.2f}"

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Violation")
        self._balance = value
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Violation")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Violation")
        if amount > self.balance:
            raise ValueError("Violation")
        self.balance -= amount
        

def main():
    Lax = BankAccount("Lax", 250)
    Lax.deposit(500)
    Lax.withdraw(100)
    print(Lax)


if __name__ == "__main__":
    main()