import numpy_financial as npf

costs = [50000,50000,10000,10000]
revenue = [5000,70000,70000,50000]
netcashflow = []

for i in range(len(costs)):
    netcashflow.append(revenue[i] - costs[i])

print(netcashflow)
discountrate = 0.07
total = []

for i in range(len(netcashflow)):
    print("Year " + str(i+1))
    x = netcashflow[i] / ((1 + discountrate) ** (i + 1))
    total.append(x)
    print(x)

##print("NPV:", sum(total))

print("\n")
irr = npf.irr(netcashflow)
print("IRR: {:.5%}".format(irr))

rounded_irr = round(irr, 5)

for i in range(len(netcashflow)):
    print("Year " + str(i+1))
    print(str(netcashflow[i]) + " /(1 + " + str(rounded_irr) + (")^") + str(i+1))
