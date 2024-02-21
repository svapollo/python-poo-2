class Account:

    def __init__(self, holder):
        self._holder = holder
        self._balance = 0
        self._active = False

    def __str__(self):
        status = "Active" if self._active else "Inactive"
        return f'Holder: {self.holder} | Balance: {self._balance} | Status: {status}'

    def activate_account(self):
        self._active = True

    @property
    def holder(self):
        return self._holder

    @property
    def balance(self):
        return self._balance

    def is_active(self):
        return self._active


account1 = Account('Apollo')
print(account1)
account2 = Account('Mayara')
print(account2)
account3 = Account('Rafael')
account3.activate_account()
print(account3)
