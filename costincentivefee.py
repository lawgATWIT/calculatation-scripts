min_fee  = 5000
max_fee = 19750
target_fee = 10000

allowable_expenses = 150000


sharing_rate = 0.10

project_cost = 190000


fee = (allowable_expenses - project_cost)* .15 + target_fee

##fee = (allowable_expenses - project_cost)* .15

if fee > max_fee:
    fee = max_fee

if fee < min_fee:
    fee = min_fee

print("fee: " + str(fee))

print("Seller paid: " + str(project_cost + fee))

print("Sellers profit: " + str(abs(project_cost - fee)))