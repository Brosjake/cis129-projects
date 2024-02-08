#Variables
cprice = 5.00
mprice = 4.00
tax = 0.06

print("Welcome to my Coffee Shop!")

#Input Variables
nc = int(input("How many coffees would you like?"))
mc = int(input("How many Muffins Would you like?"))

print("Thankyou for shopping with us, here is your reciept\n\n")


subtotal = (nc*cprice) + (mc*mprice)
#Format to two decimal points
formatcoffee =  f"{nc*cprice:.2f}"
formatmuffins =  f"{mc*mprice:.2f}"

#Receipt:
print("My coffee and Muffin Shop Receipt")
print(nc, "Coffee at $5 each: $" , formatcoffee)
print(mc,  "Coffee at $4 each: $", formatmuffins)
print("6% tax: $",round(tax*subtotal,2) )
print("#---------")
print("Total: $",round((tax*subtotal + subtotal),2))

