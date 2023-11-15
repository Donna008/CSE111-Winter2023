from datetime import datetime
DISC_RATE = 0.10
SALES_TAX_RATE = 0.06

#day_of_week = 3
#print(day_of_week)
subtotal= float(input("please enter the subtotal:"))
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
if subtotal >= 50 and (day_of_week == 1 or day_of_week == 2):
    discount = round(subtotal * DISC_RATE, 2)
    #discount_amount = subtotal * 0.1
    print(f"discount amount: {discount:.2f}")
    
    #print(f"sales tax is: {sales_tax: 0.2}")
    subtotal -= discount

#sales_tax = (subtotal - discount) * 0.06
sales_tax = round(subtotal * SALES_TAX_RATE,2)
    #sales_tax_amount = (subtotal * sales_tax)
print(f"sales tax amount: {sales_tax:.2f}")
total = subtotal + sales_tax
print(f"total:{total:.2f}")