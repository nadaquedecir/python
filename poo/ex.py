
class BankAccount:
    interest_rate = 0.02
    
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
    
    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print("Interest cambiado")
    
    @staticmethod
    def validate_amount(amount):
        return amount > 0
    
    def withdraw(self, amount):
        if self.validate_amount(amount): # aqui se ingreso al static method de forma interna
            if self.balance >= amount:
                self.balance -= amount
                print("Retiro exitoso")
            else:
                print("Saldo insuficiente")
        else:
            print("Error. Monto ingresado incorrecto. Monto debe ser mayor a cero")


account_1 = BankAccount("BENJAMIN", 2000)
account_2 = BankAccount("Simon", 3000)

print(BankAccount.interest_rate)
BankAccount.change_interest_rate(0.03)
print(BankAccount.interest_rate)

account_1.withdraw(1500)
account_2.withdraw(3500)


# function vs method 
# function funciona de forma independiente
# method depende de una instancia, un objeto para ser llamada