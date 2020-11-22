expenses = int(input())
income = int(input())
profit = income - expenses
if profit > 0:
    print(f"company profit = {profit}")
    print(f"profitability = {profit / income:.2f}")
    people_num = int(input("num of employees:"))
    print(f"one person profit:{profit / people_num:.2f}")
elif profit < 0:
    print (f"company loss = {profit}")
else:
    print("compony profit goes to 0")