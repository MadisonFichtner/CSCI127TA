# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Lab 2: Tax Calculator
# Your Name
# Date: January 25, 2018
# ---------------------------------------
# Calculate the amount of tax owed by a
# single taxpayer in 2018. 
# ---------------------------------------


# The missing Python function goes here.


# ---------------------------------------

def process(income):
    print("In tax year 2017, you earned ${:.2f}".format(income))
    tax_owed = calculate_tax(income)
    print("Your tax bill is ${:.2f}\n".format(tax_owed))

#---------------------------------------

def main():
    process(500)
    process(10000)
    process(50000)
    process(100000)
    process(175000)
    process(250000)
    process(500000)
    process(750000)

# ---------------------------------------

main()
