costs = [50000,50000,10000,10000]
revenue = [5000,70000,70000,50000]

net_cash_flow = 0
net_cash_flow_list = []

for i in range(len(costs)):
    net_cash_flow += revenue[i] - costs[i]
    net_cash_flow_list.append(net_cash_flow)

for year, total_cash_flow in enumerate(net_cash_flow_list, start=1):
    print(f"Year {year}: Running Total Net Cash Flow = ${total_cash_flow}")
