def calculate_tax(income):
    ''' Calculate tax owed based on marginal tax rates for the given income. '''
    if income > 500000:
        return (income - 500000) * .37 + calculate_tax(500000)
    elif income > 200000:
        return (income - 200000) * .35 + calculate_tax(200000)
    elif income > 157500:
        return (income - 157500) * .32 + calculate_tax(157500)
    elif income > 82500:
        return (income - 82500) * .24 + calculate_tax(82500)
    elif income > 38700:
        return (income - 38700) * .22 + calculate_tax(38700)
    if income > 9525:
        return (income - 9525) * .12 + calculate_tax(9525)
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
