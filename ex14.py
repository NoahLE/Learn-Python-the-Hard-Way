from sys import argv

script, user_name, human = argv
# prompt = '> '
prompt = '<<<{(O=O)}>>>: '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Are you a human? {0}? Really? I don't believe you.".format(human)
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)

# Study drills
# 1. Zork - http://thcnet.net/zork/index.php | Adventure - http://my.ign.com/atari/adventure