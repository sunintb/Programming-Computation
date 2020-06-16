# This program calculates and displays the first year where Brutus' bank balance overtakes Portia's balance
# and their balances in that respective year
# Program Name: sa3problem2
# Author: Sunint Bindra
# January 12, 2019
# Computer Science 1


# The constants and variables used to calculate Brutus' wealth
BRUTUS_INITIAL_DEPOSIT = 1
BRUTUS_INTEREST_RATE = 5
brutus_wealth = BRUTUS_INITIAL_DEPOSIT

# The constants and variables used to calculate Portia's wealth
PORTIA_INITIAL_DEPOSIT = 100000
PORTIA_INTEREST_RATE = 4
portia_wealth = PORTIA_INITIAL_DEPOSIT

# The year we start at
year = 0


while portia_wealth > brutus_wealth:
    brutus_wealth = brutus_wealth * (1 + BRUTUS_INTEREST_RATE / 100)
    portia_wealth = portia_wealth * (1 + PORTIA_INTEREST_RATE / 100)
    year = year + 1

# The print statements below generate the output with the year Brutus
# overtakes Portia and their respective balances in that year
print("Brutus overtakes Portia's wealth in year " + str(year) + " A.D.")
print("Portia's balance is " + str(portia_wealth) + " in the year " + str(year) + " A.D.")
print("Brutus' balance is " + str(brutus_wealth) + " in the year " + str(year) + " A.D.")
