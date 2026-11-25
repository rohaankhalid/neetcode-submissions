class Account:
    def __init__(self, title: str, balance: float):
        self.title = title      # public attribute
        self._balance = balance # protected attribute
    
    def display_balance(self) -> None:
        print(f"Balance: ${self._balance}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
