
#Melanie MacNicol
# Assignment01
# Part1
# Add Python code to do the following
# Create a variable called foods and assign it a list of at least three strings that name some of your favorite foods. Make these strings all lowercase.
# Add a print statement that prints out the last element in the list foods
# Use append to add one more food name to foods
# Add a print statement that uses a slice to print all but the first element in foods

foods=['cake','carrots','coffee']
print(foods)
print(foods[2])
foods.append('cookies')
print(foods)
print(foods[1:])

# Part2
# Using a for loop and a print statement inside the loop, output a message with the the elements in your list, one per line of output.
# Using a loop very much like the one in the previous step, output a message with the the elements in your list capitalized (you should use the string method capitalize()), one per line of output.

for food in foods:
    print(food)
for food in foods:
    print(food.capitalize())

# Part3
# Create a variable called foods_tup and assign it a tuple containing the same strings that you put into the list foods in Part 1. Print out the tuple's contents.
# Remember that you can't use append on a tuple because tuples are immutable. Change what is stored in the variable foods_tup so that is a tuple with one more element than previously. Print the new tuple's contents.

foods_tup=('cake','carrots','coffee')
print(foods_tup)
foods_tup=('cake','carrots','coffee','cookies')
print(foods_tup)

# Part4
# Add Python code to do the following:
# Using append, add one more tuple to vacc_counties that represents an additional county and its vaccination rate. You may use Scott County, which currently has a rate of 28.1%, or you may look up another county's data if you like.
# Using a for loop and an if statement, go through vacc_counties and print out a message for those counties that have a higher than 30% vaccination rate.

vacc_counties = [('Pulaski', 42.7), ('Benton', 41.4), ('Fulton', 22.1), ('Miller', 9.6), ('Mississippi', 29.4)]
print(vacc_counties)
vacc_counties.append(('Scott', 28.1))
print(vacc_counties)
for county in vacc_counties:
    if county[1]>30:
        print(f'{county[0]} is doing well with a vaccination rate of {county[1]}.')
    else:
        print(f'{county[0]} needs to up its game from that rate of {county[1]}.')

# Bonus:
from statistics import mean
numbers=[]
print(numbers)
for county in vacc_counties:
    numbers.append(county[1])
print(f'The mean vaccination rate of these counties is {mean(numbers)}%.' )

