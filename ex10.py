tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# added a break statement
while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,
    break

# study drills
# 2. http://stackoverflow.com/a/7783116/3192322
print '''
THIS DOESN'T DO SOMETHING :D
'''

print """
THIS "DOES" SOMETHING TOO :D
"""
# 3.
print "\t\t**\t**\t**\n\t\t\/\t\\/\t\/\n\t\t_________"
# 4.
print "r: %r \ns: %s" % ("'", "'")
print "r: %r \ns: %s" % ('"', '"')