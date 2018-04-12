import matplotlib.pyplot as plt

def compound_interest(p,r,n,t):
    return p*(1+(r/n))**(n*t)

def interest_over_years(r):
    compound = []
    for t in range(51):
        compound.append(compound_interest(100,r,1,t))
    return compound
    
years = [2018+i for i in range(51)]

fig = plt.gcf()
fig.canvas.set_window_title('Compound Interest Display for Starting Amount of $100')
plt.xlabel('Year')
plt.ylabel('Dollars')
plt.plot(years, interest_over_years(.05), 'k+', label='5% interest')
plt.plot(years, interest_over_years(.1), 'b+', label='10% interest')
plt.legend(loc='upper left')
plt.show()
