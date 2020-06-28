income = int(input())
tax = 0
if 0 <= income <= 15527:
    tax = 0
    total = 0
elif 15528 <= income <= 42707:
    tax = 15
    total = round(income * .15)
elif 42708 <= income <= 132406:
    tax = 25
    total = round(income * .25)
elif income >= 132407:
    tax = 28
    total = round(income * .28)
print("The tax for {amount} is {percent}%. That is {calculated_tax} dollars!".format(amount=income, percent=tax, calculated_tax=total))