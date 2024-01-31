costs = [100000,10000,10000,10000]
revenue = [0,5000,50000,110000]

discount_rate = 0.07

discount_costs = []
discount_revenue = []

for i in range(len(costs)):
    x = costs[i] * ((1 / (1 + discount_rate)) ** (i + 1))
    discount_costs.append(x)

for i in range(len(revenue)):
    x = revenue[i] * ((1 / (1 + discount_rate)) ** (i + 1))
    discount_revenue.append(x)
print("discounted costs: ")
print(discount_costs)
print("Total: " + str(sum(discount_costs)))

print("discounted benefits")
print(discount_revenue)
print("Total: " + str(sum(discount_revenue)))
discount_cash_flow = []

ROI = (sum(discount_revenue) - sum(discount_costs))/sum(discount_costs)
print(ROI)
print(str(ROI*100) + "%")