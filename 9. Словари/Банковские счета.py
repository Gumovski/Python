bank_client = {}
def deposit(name,summ):
    if name not in bank_client:
        bank_client[name] = 0
    bank_client[name] += summ
def withdraw(name,summ):
    if name not in bank_client:
        bank_client[name] = 0
    bank_client[name] -= summ
def balance(name):
    if name not in bank_client:
        return "ERROR"
    return bank_client[name]
def transfer(from_name, to_name, summ):
    if from_name not in bank_client:
        bank_client[from_name] = 0
    if to_name not in bank_client:
        bank_client[to_name] = 0
    bank_client[from_name] += summ
    bank_client[to_name] -= summ
def income(percent):
    for name in bank_client:
        new_balance = bank_client[name]
        if new_balance > 0:
            bank_client[name] += (new_balance * percent) // 100