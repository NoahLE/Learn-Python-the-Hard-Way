def number_loop(max_number, increment):
    numbers = []
    for i in range(0, max_number + 1, increment):
        numbers.append(i)
    return numbers

print number_loop(6, 2)

# =============================================

# def number_loop(max_number, increment):
#     i = 0
#     numbers = []
#     while i <= max_number:
#         numbers.append(i)
#         i += increment
#     return numbers
#
# print (number_loop(6, 2))

# =============================================

# i = 0
# numbers = []
#
# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)
#
#     i += 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i
#
#
# print "The numbers: "
#
# for num in numbers:
#     print num
