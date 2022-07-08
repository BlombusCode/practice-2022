from multiprocessing.dummy import active_children
from time import time
from venv import create
import PySimpleGUI as sg

def create_window():
    sg.theme('black')
    layout = [
    [sg.VPush()],
    [sg.Image('cross.png', pad=0,enable_events = True,key='-CLOSE-')],
    [sg.Text('Add Minute',font='Franklin 20',key='-ADDMINUTE-', enable_events= True),sg.Text('Add Hour',font='Franklin 20',key='-ADDHOUR-')],
    [sg.Text('$0.00',font='Franklin 20',key='-TOTAL-')],
    [sg.Input(key='-INPUT-')],
    [sg.Button('Start', button_color=('#FFFFFF','#FF0000'),border_width=0,key='-STARTSTOP-')],
    [sg.VPush()]
    
    ]
    return sg.Window('Money Machine', layout,size=(300,300),no_titlebar = False,element_justification='center')

def wage_per_second(wage,elapsed_time):
    secondly_wage = (wage / 3600)#Converts wage to seconds
    total = str(round((secondly_wage * elapsed_time),2))#Multiples time and wage per second, rounding to .00

#TODO: Elapsed time as Hour/Minute/Second

    wageupdate = ('$',total,'Time', elapsed_time)#Store as tuple to pass to string concatenation
    delimiter = ' '
    

    return delimiter.join([str(value) for value in wageupdate])#List comprehension to convert tuple to string and print return.


window = create_window()
active = False
elapsed_time = 0
total_time = 0
#start_time = 0
while True:
    event, values = window.read(timeout=10)
    
#START/STOP PROGRAM

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

#TIME AND MONEY UPDATES

    if active:#Detects if active before updating screen
        input_value = values['-INPUT-']
        if input_value.isnumeric():


            if event == '-ADDMINUTE-':#TODO: Fix functionality
                print(elapsed_time)
                #TODO: Does not add to timer, nor money
                #elapsed_time = total_time + 60 - start_time <-- this should work
                elapsed_time = round((time() + 60) - start_time, 1)#TODO:Cannot add to time - need to create variable for storing time updates.
                window['-TOTAL-'].update(wage_per_second(int(input_value), elapsed_time))
                print(elapsed_time)
                

            elapsed_time = round(time() - start_time,1)#Difference between times
            window['-TOTAL-'].update(wage_per_second(int(input_value),elapsed_time))

window.close()


#TODO GUI improvements
#TODO Reset - Change Wage