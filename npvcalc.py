
costs = [50000,50000,10000,10000]
revenue = [5000,70000,70000,50000]
netcashflow = []
i = 0

for i in range(len(costs)):
     netcashflow.append(revenue[i] - costs[i])

print(netcashflow)
discountrate = 0.07
total = []

for i in range(len(netcashflow)):
    print("Year " + str(i+1))
    x = netcashflow[i]/((1+discountrate)**(int(i)+1))
    total.append(x)
    print(x)
    
print("NPV: " + str(sum(total)))

