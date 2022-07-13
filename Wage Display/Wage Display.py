from time import time
import PySimpleGUI as sg

def create_window():
    sg.theme('DarkGrey10')
    layout = [
    [
    sg.Button('+1 Minute',font='Franklin 10',key='-ADDMINUTE-', enable_events= True),sg.Button('+5 Minutes',font='Franklin 10',key='-ADD5MINUTE-', enable_events= True),
    sg.Button('+1 Hour',font='Franklin 10',key='-ADDHOUR-',enable_events= True),sg.Button('+2 Hours',font='Franklin 10',key='-ADD2HOUR-',enable_events= True)
    ],
    [sg.Text('$0.00',font='Franklin 20',key='-TOTAL-')],
    [sg.Input(key='-INPUT-')],
    [sg.Button('Start', button_color=('#FFFFFF','#FF0000'),border_width=0,key='-STARTSTOP-')],
    [sg.VPush()]
    
    ]
    return sg.Window('Money Machine', layout,size=(500,150),no_titlebar = False,element_justification='center')

def wage_time(wage,elapsed_time):
    #Calculates monetary value
    secondly_wage = (wage / 3600)#Converts wage to seconds
    total = round((secondly_wage * elapsed_time),2)#Multiples time and wage per second, rounding to .00

    #Calculates elapsed time
    hours = elapsed_time // 3600
    elapsed_time -= hours*3600
    minutes = elapsed_time // 60
    seconds = elapsed_time - minutes*60
    #Convert time into 00.00.00 format
    hours_print = str(round(hours)).zfill(2)
    minutes_print = str(round(minutes)).zfill(2)
    seconds_print = str(round(seconds)).zfill(2)

    
    wageupdate = ('$',"%.2f" % total,' Time: ', hours_print,':', minutes_print,':',seconds_print)# hour, ' Hour', minute, ' Minute', seconds, ' Seconds')#Store as tuple to pass to string concatenation
    delimiter = ''
    

    return delimiter.join([str(value) for value in wageupdate])#List comprehension to convert tuple to string and print return.


window = create_window()
active = False
elapsed_time = 0
total_time = 0
minutes_added = 0
hours_added = 0

while True:
    event, values = window.read(timeout=10)
    
#START/STOP PROGRAM

    if event == sg.WIN_CLOSED:
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
                minutes_added = 0
                hours_added = 0
                window['-STARTSTOP-'].update('Start')

#TIME AND MONEY UPDATES

    if active:#Detects if active before updating screen
        input_value = values['-INPUT-']
        if input_value.isnumeric():

            
            if event == '-ADDMINUTE-':#Increments minutes
                minutes_added += 1
            if event == '-ADD5MINUTE-':#Increments minutes
                minutes_added += 5
            if event == '-ADDHOUR-':#Increments minutes
                hours_added += 1
            if event == '-ADD2HOUR-':#Increments minutes
                hours_added += 2

                
            total_time = time() + (60 * minutes_added) + (3600 * hours_added)
            elapsed_time = round(total_time - start_time,1)#Calculates difference between current and start time
            window['-TOTAL-'].update(wage_time(int(input_value),elapsed_time))#Updates -TOTAL- display

window.close()