import time

def wage_per_sec(hourly_wage):#Calculates wage per second
    secondly_wage = (hourly_wage /3600) # 60 min in hour 60 seconds in min - 60*60 = 3600 |  wage /3600 = wage per second
    return secondly_wage

def print_wage_second(secondly_wage):
    total = 0
    while total < 19.00:
        total += secondly_wage
        print('$', round(total,3))
        time.sleep(1.0)


wage = input('Enter hourly wage:')
print(wage)
print_wage_second(wage_per_sec(float(wage)))

#TODO GUI