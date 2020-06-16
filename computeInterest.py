# This program computes the wealth in Brutus' account by the year 2019 A.D.
# Program Name: sa3problem1
# Author: Sunint Bindra
# January 12, 2019
# Computer Science 1


# The initial amount in Brutus' bank account in year 0 A.D.
BRUTUS_INITIAL_DEPOSIT = 1

# The interest rate Brutus received for his bank account
BRUTUS_INTEREST_RATE = 5

# Defining the variables used in the wealth calculations
brutus_wealth = BRUTUS_INITIAL_DEPOSIT

# The year we start at
year = 0


while year < 2019:
    brutus_wealth = brutus_wealth * (1 + BRUTUS_INTEREST_RATE/100)
    year = year + 1

# The print statement below generates the output with the year and corresponding money in account
print("At year " + str(year) + " A.D., the balance in Brutus' account is " + str(brutus_wealth))
