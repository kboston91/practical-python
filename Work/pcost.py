# pcost.py
#


p = open('Data/portfolio.csv', 'rt')
headers = next(p).split(',')
print(headers)
total_cost = 0

for line in p:
    row = line.split(',')
    share_cost= round(int(row[1]) * float(row[2]), 2)
    total_cost = total_cost + share_cost
    print('The cost to buy ', row[0], ' would be ', share_cost)
print('The cost to buy this portfolio is ', total_cost)

p.close()
# Exercise 1.27
