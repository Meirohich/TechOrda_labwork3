import enum


class Account(enum.Enum):
    USD = 'USD'
    RUB = 'RUB'
    KZT = 'KZT'
    EUR = 'EUR'


class Bank:

    def init(self):
        self.name = ''
        self.surname = ''
        self.account = ''
        self.balance = 0


    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_balance(self):
        return self.balance

    def get_account(self):
        return self.account

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_balance(self, balance):
        self.balance = balance

    def set_account(self, account):
        self.account = account

    def addBalance(self, balance):
        self.balance += balance

    def subBalance(self, balance):
        self.balance -= balance

    def convert(self, balance, m1, m2):
        if m1 == 'USD' and m2 == 'KZT':
            print(f'{balance, m1} to {balance * 470, m2}')
        elif m1 == 'RUB' and m2 == 'KZT':
            print(f'{balance, m1} to {balance * 8, m2}')
        elif m1 == 'KZT' and m2 == 'USD':
            print(f'{balance, m1} to {balance / 470, m2}')

    def str(self):
        return f'Bank account of {self.get_surname(), self.name}.Balance {self.balance, self.account}'

    def register(self):
        surnname = str(input('Type Surname '))
        name = str(input('Type Name '))
        account = str(input('Type Account ')).upper()
        for curs in Account:
            if curs.value == account:
                self.set_surname(surnname)
                self.set_name(name)
                self.set_account(account)


bank = Bank()
bank.register()
bank.addBalance(123)
bank.subBalance(213)
bank.convert(300, 'USD', 'KZT')
print(bank.str())