def calculate_tax(income):
    if income > 500000:
        return income * .37
    elif income > 200000:
        return income * .35
    elif income > 157500:
        return income * .32
    elif income > 82500:
        return income * .24
    elif income > 38700:
        return income * .22
    elif income > 9525:
        return income * .12
    else:
        return income * .1

def process(income):
    print("In tax year 2018, you earned ${:.2f}".format(income))
    tax_owed = calculate_tax(income)
    print("Your tax bill is ${:.2f}\n".format(tax_owed))

def main():
    process(500)
    process(10000)
    process(50000)
    process(100000)
    process(175000)
    process(250000)
    process(500000)
    process(750000)

main()
