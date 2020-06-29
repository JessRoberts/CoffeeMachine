income = int(input())
bracket = 0
percent = 0
calculated_tax = 0

if income == 0 or income <= 15527:
    bracket = 0
    percent = 0
    calculated_tax = income * bracket
elif income == 15528 or income <= 42707:
    bracket = 0.15
    percent = 15
    calculated_tax = income * bracket
elif income == 42708 or income <= 132406:
    bracket = 0.25
    percent = 25
    calculated_tax = income * bracket
elif income >= 132407:
    bracket = 0.28
    percent = 28
    calculated_tax = income * bracket

print(f'The tax for {income} is {percent}%. That is {calculated_tax:.0f} dollars!')
