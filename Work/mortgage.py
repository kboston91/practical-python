# mortgage.py
#
# Exercise 1.7
principal = 500000.00
rate = 0.05
payment = 2684.11
extra_payment = 1000.00
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
months_paid = 0

# for i in range(60):
#     principal = principal * (1+rate/12) - payment
#     total_paid = total_paid + payment
#     months_paid = months_paid + 1
#     print(months_paid, 'Total paid', round(total_paid, 2),'Principal', round(principal,2))
# #print('Total paid', round(total_paid, 2), 'Months paid', months_paid)

# for i in range(extra_payment_start_month,extra_payment_end_month):
#     principal = principal * (1+rate/12) - (payment + extra_payment)
#     total_paid = total_paid + payment + extra_payment
#     months_paid = months_paid + 1
#     print(months_paid, 'Total paid', round(total_paid, 2),'Principal', round(principal,2))
# #print('Total paid for first 12 months', round(total_paid, 2), months_paid)

while principal > 0:
   
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months_paid = months_paid + 1
    
    if months_paid >= extra_payment_start_month and months_paid <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    if principal <= 0:
        payment = principal
        principal = principal - payment  

    print(f'Months paid - {months_paid}, Total paid - {round(total_paid, 2)}, Principal - {round(principal,2)}')
    

 
    
    
