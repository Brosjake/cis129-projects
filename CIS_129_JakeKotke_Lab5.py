#Jake Kotke, 3/14, This program will calculate the total payout and recieve botal inputs from the user

# Lab 5 The Bottle Return Program


keepGoing = 'y'

#This is my while loop that is designed to run seven times
while keepGoing == 'y':
    counter = 1
    totalBottles = 0
    todayBottles = 0
    totalPayout = 0
    while(counter <= 7):
    #This code gets the bottles of the day
        todayBottles = int(input(f'Enter number of bottles for day #{counter}: '))
    #This code adds the today bottles to the total bottles
        totalBottles = totalBottles + todayBottles
    #This is my loop counter
        counter = counter + 1
#Calculation to get the total payout
    totalPayout = totalBottles/10
    print(f'\nThe total number of bottles collected is {totalBottles}')
    print(f'The total paid out is $ {totalPayout}')

    keepGoing = input("\nDo you want to enter another week’s worth of data? (Enter y or n): ")
