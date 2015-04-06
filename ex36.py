from sys import exit

def solve_tickets():
    print 'How many tickets are in the inbox?'
    ticket_number = raw_input("> ")

    if ticket_number > 0:
        print 'Solving tickets...'
    else:
        print 'Woo, no tickets. Time to work'

    go_home()


def do_task():
    print 'What do you want to work on?'
    task = raw_input("> ")

    if task == 'docs':
        print 'Working on docs.'
    elif task == 'knowledge':
        print 'Ask a dev'
    else:
        print "Finding something that's broken"

    go_home()


def go_home():
    print 'Have you worked enough?'
    go_home = raw_input("> ")

    if go_home == 'yes':
        print 'Have a good day!'
        exit(0)
    else:
        arrive_at_work()

def arrive_at_work():
    print 'Welcome back! What do you want to do?'
    work_task = raw_input("> ")

    if work_task == 'tickets':
        print 'Heading over to solve tickets'
        solve_tickets()
    elif work_task == 'task':
        print 'Yay! No tickets'
        do_task()

arrive_at_work()