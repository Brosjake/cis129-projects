#Variables
cprice = 5.00
mprice = 4.00
jprice = 2.00
wprice = 1.50
tax = 0.06

print("Welcome to my Coffee Shop!")

#Input Variables
nc = int(input("How many coffees would you like?"))
mc = int(input("How many Muffins Would you like?"))
wc = int(input("How many Water Bottles would you like?"))
jc = int(input("How many Apple Juice's Would you like?"))


print("Thankyou for shopping with us, here is your reciept\n\n")


subtotal = (nc*cprice) + (mc*mprice) + (jc*jprice) + (wc*wprice)
#Format to two decimal points
formatcoffee =  f"{nc*cprice:.2f}"
formatmuffins =  f"{mc*mprice:.2f}"
formatwater =  f"{wc*wprice:.2f}"
formatjuice =  f"{jc*jprice:.2f}"

#Receipt:
print("My coffee and Muffin Shop Receipt")
print(nc, "Coffee at $5 each: $" , formatcoffee)
print(mc,  "Muffins at $4 each: $", formatmuffins)
print(wc, "Water at $1.50 each: $" , formatwater)
print(jc,  "Juice at $2 each: $", formatjuice)

print("6% tax: $",round(tax*subtotal,2) )
print("#---------")
print("Total: $",round((tax*subtotal + subtotal),2))

