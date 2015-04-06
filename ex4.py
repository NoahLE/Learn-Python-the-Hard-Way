# assigns integers to variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# calculates various car stats
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# prints out the car stats
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Study drill
# Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#     average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

# line 8's car_pool_capacity is a variable that does not exist, it should be
# carpool_capacity

# I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
# No, 4.0 does not need to be a floating point number because you can't have half a seat or part of a driver.
# The equation on line 10 only multiplies the values so it will always produce an integer

# please note the difference between = and == (assignment vs comparison)
