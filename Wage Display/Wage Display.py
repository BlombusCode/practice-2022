from time import time
import PySimpleGUI as sg

def create_window():
    sg.theme('black')
    layout = [
    [sg.Image('cross.png', pad=0,enable_events = True,key='-CLOSE-')],
    [sg.Text('Add Minute',font='Franklin 20',key='-MINUTE-'),sg.Text('Add Hour',font='Franklin 20',key='-HOUR-')],
    [sg.Text('MONEY',font='Franklin 20',key='-TOTAL-')],
    [sg.Input(key='-INPUT-')],
    [sg.Button('Start', button_color=('#FFFFFF','#FF0000'),border_width=0,key='-STARTSTOP-')]
    
    ]
    return sg.Window('Money Machine', layout,size=(300,300),no_titlebar = False,element_justification='center')

def wage_per_second(wage,elapsed_time):
    secondly_wage = (wage / 3600)#Converts wage to seconds
    total = str(round((secondly_wage * elapsed_time),2))#Multiples time and wage per second, rounding to .00

    return ('$',total,'Time', elapsed_time)#Returns as string to update screen



def deprecated_wage_per_second(wage):
    secondly_wage = (wage /3600)
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
        return('$', round(total,3), '|',minutes, 'Minute(s)', seconds, "Second(s)" )


def add_minute():
    int = 0
    #empty function for now

def add_hour():
    int = 0
    #empty function for now

window = create_window()
active = False
start_time = 0
while True:
    event, values = window.read(timeout=10)
    
    if event in(sg.WIN_CLOSED,'-CLOSE-'):
        break
    if event == '-STARTSTOP-':
        if active == False:#Start to active
            start_time = time()#Update start time
            active = True
            window['-STARTSTOP-'].update('Stop')


    input_value = values['-INPUT-']
    if input_value.isnumeric():
        elapsed_time = round(time() - start_time,1)#Difference betwwne times
        window['-TOTAL-'].update(wage_per_second(int(input_value),elapsed_time))


""" wage = float(input('Enter hourly wage:'))
while True:#TODO Async input

    print('Enter 1 to print add a minute \n Enter 2 to add an hour \n Enter 3 at any time to stop the program.')
    print_wage_second(wage_per_sec(wage),wage)
    status = int(input())
    if status == 1:
        add_minute()
    elif status == 2:
        add_hour()
    elif status == 3:
        running = False
        break
 """
window.close()


#TODO GUI
#TODO Stop - Reset - Change Wage