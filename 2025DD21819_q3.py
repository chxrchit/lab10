class Bank:
    def __init__(self):
        self.accounts = {}
        self.users_count = 0

    def open_account(self, owner, initial_balance):
        self.users_count += 1
        self.accounts[owner] = initial_balance

    def deposit(self, owner, amount):
        if amount > 0:
            if (owner in self.accounts):
                self.accounts[owner] += amount

    def withdraw(self, owner, amount):
        if owner in self.accounts:
            if self.accounts[owner] - amount < 0 or amount <= 0:
                print('Invalid withdrawal')
                return
            self.accounts[owner] -= amount

    def get_balance(self, owner):
        if (owner in self.accounts):
            return (self.accounts[owner])
        else:
            return(0)

    def get_users_count(self):
        return (self.users_count)

bank = Bank()
k = int(input())

for i in range(k):
    query = input().split()
    cmd = query[0]

    if cmd == "OPEN_ACCOUNT":
        bank.open_account(query[1], int(query[2]))
    elif cmd == "DEPOSIT":
        bank.deposit(query[1], int(query[2]))
    elif cmd == "WITHDRAW":
        bank.withdraw(query[1], int(query[2]))
    elif cmd == "GET_BALANCE":
        print(bank.get_balance(query[1]))
    elif cmd == "USERS_COUNT":
        print(bank.get_users_count())
