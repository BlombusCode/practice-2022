from multiprocessing.dummy import active_children
from time import time
from venv import create
import PySimpleGUI as sg

def create_window():
    sg.theme('black')
    layout = [
    [sg.Image('cross.png', pad=0,enable_events = True,key='-CLOSE-')],
    [sg.Text('Add Minute',font='Franklin 20',key='-MINUTE-'),sg.Text('Add Hour',font='Franklin 20',key='-HOUR-')],
    [sg.Text('$0.00',font='Franklin 20',key='-TOTAL-')],
    [sg.Input(key='-INPUT-')],
    [sg.Button('Start', button_color=('#FFFFFF','#FF0000'),border_width=0,key='-STARTSTOP-')]
    
    ]
    return sg.Window('Money Machine', layout,size=(300,300),no_titlebar = False,element_justification='center')

def wage_per_second(wage,elapsed_time):
    secondly_wage = (wage / 3600)#Converts wage to seconds
    total = str(round((secondly_wage * elapsed_time),2))#Multiples time and wage per second, rounding to .00

#TODO: Elapsed time as Hour/Minute/Second

    wageupdate = ('$',total,'Time', elapsed_time)#Store as tuple to pass to string concatenation
    delimiter = ' '
    

    return delimiter.join([str(value) for value in wageupdate])#List comprehension to convert tuple to string and print return.


def add_minute():
    int = 0
    #empty function for now

def add_hour():
    int = 0
    #empty function for now

window = create_window()
active = False
#start_time = 0
while True:
    event, values = window.read(timeout=10)
    
    if event in(sg.WIN_CLOSED,'-CLOSE-'):
        break
    if event == '-STARTSTOP-':
        if active == False:#Start
            start_time = time()#Update start time (Each new start resets time, no need to manually correct)
            active = True
            window['-STARTSTOP-'].update('Stop')
        else:
            #If already active we stop
            if active == True:#Stop
                active = False
                window['-STARTSTOP-'].update('Start')



    if active:#Detects if active before updating screen
        input_value = values['-INPUT-']
        if input_value.isnumeric():#TODO: Refactor so that program does not start until "start" is hit
            elapsed_time = round(time() - start_time,1)#Difference between times
            window['-TOTAL-'].update(wage_per_second(int(input_value),elapsed_time))

window.close()


#TODO GUI improvements
#TODO Stop - Reset - Change Wage