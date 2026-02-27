class BankAccount:
    def __init__(self, Balance):
        self.__balance = Balance
    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
print("Saldo awal:", acc.get_balance())

