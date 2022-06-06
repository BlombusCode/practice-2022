from os import stat
import time

def wage_per_sec(hourly_wage):#Calculates wage per second
    secondly_wage = (hourly_wage /3600) # 60 min in hour 60 seconds in min - 60*60 = 3600 |  wage /3600 = wage per second
    return secondly_wage

def print_wage_second(secondly_wage,wage):
    total = 0
    seconds = 40
    minutes = 0
    while total < wage:
        if seconds != 0 and minutes != 0:
            total = (secondly_wage * ((seconds) + (minutes * 60)))
        elif seconds != 0:
            total = (secondly_wage * seconds)
        elif minutes != 0:
            total = secondly_wage * (minutes * 60)
        
        seconds+= 1
        if seconds % 60 == 0:
            minutes += 1
            seconds = seconds - 60
        print('$', round(total,3), '|',minutes, 'Minute(s)', seconds, "Second(s)" )
        time.sleep(1.0)


def add_second():
    int = 0
    #empty
def add_minute():
    int = 0
    #empty function for now


running = True
wage = float(input('Enter hourly wage:'))

while running == True:#TODO Async input

    print('Enter 1 to print add a minute \n Enter 2 to add an hour \n Enter 3 at any time to stop the program.')
    print_wage_second(wage_per_sec(wage),wage)
    status = int(input())
    if status == 1:
        add_second()
    elif status == 2:
        add_minute()
    elif status == 3:
        running = False
        break

    


#TODO GUI
#TODO Stop - Reset - Change Wage