# To run this script, you need to install Python3, Python3-tk and PySimpleGUI.

import PySimpleGUI as sg

sg.theme ("DarkGrey5")
layout = [  [sg.Text("LENGHT")],
            [sg.InputText(size=(4,1), key='length'), sg.Combo(['mm', 'cm', 'dm', 'm', 'km', 'in', 'ft', 'yd', 'mile', 'NM'], key='dm1'), sg.Text('TO'), sg.Combo(['mm', 'cm', 'dm', 'm', 'km', 'in', 'ft', 'yd', 'mile', 'NM'], key='dm2')],
            [sg.Button("CONVERT LENGTH"), sg.Text('', text_color='yellow', key='LENGTHCALC')],
            [sg.HorizontalSeparator()],
            [sg.Text("AREA")],
            [sg.InputText(size=(4,1), key='area'), sg.Combo(['m2', 'a', 'ha', 'km2', 'in2', 'ft2', 'yd2', 'arce', 'square mile'], key='dm3'), sg.Text('TO'), sg.Combo(['m2', 'a', 'ha', 'km2', 'in2', 'ft2', 'yd2', 'arce', 'square mile'], key='dm4')],
            [sg.Button("CONVERT AREA"), sg.Text('', text_color='yellow', key='AREACALC')],
            [sg.HorizontalSeparator()],
            [sg.Text("SPEED")],
            [sg.InputText(size=(4,1), key='speed'), sg.Combo(['m/s', 'km/h', 'mph', 'kt', 'ft/s'], key='dm5'), sg.Text('TO'), sg.Combo(['m/s', 'km/h', 'mph', 'kt', 'ft/s'], key='dm6')],
            [sg.Button("CONVERT SPEED"), sg.Text('', text_color='yellow', key='SPEEDCALC')],
            [sg.HorizontalSeparator()],
            [sg.Text("TEMPERATURE")],
            [sg.InputText(size=(4,1), key='temp'), sg.Combo(['°C', '°F', 'K'], key='dm7'), sg.Text('TO'), sg.Combo(['°C', '°F', 'K'], key='dm8')],
            [sg.Button("CONVERT TEMPERATURE"), sg.Text('', text_color='yellow', key='TEMPCALC')],
            [sg.HorizontalSeparator()],
            [sg.Text("TIME")],
            [sg.InputText(size=(4,1), key='time'), sg.Combo(['second', 'minute', 'hour', 'day', 'week'], key='dm9'), sg.Text('TO'), sg.Combo(['second', 'minute', 'hour', 'day', 'week'], key='dm10')],
            [sg.Button("CONVERT TIME"), sg.Text('', text_color='yellow', key='TIMECALC')],
            [sg.HorizontalSeparator()],
            [sg.Text("FUEL ECONOMY")],
            [sg.InputText(size=(4,1), key='fuel'), sg.Combo(['L/100km', 'US mpg', 'I mpg'], key='dm11'), sg.Text("TO"), sg.Combo(['L/100km', 'US mpg', 'I mpg'], key='dm12')],
            [sg.Button("CONVERT FUEL ECONOMY"), sg.Text('', text_color='yellow', key='FUELCALC')],
            [sg.HorizontalSeparator()],
            [sg.Button("CLEAR"), sg.Button("EXIT")]
    ]

window = sg.Window("UNIT CONVERTER").Layout(layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "EXIT":
        break
    if event == "CONVERT LENGTH": # convert units of length
        length = values['length']
        if length == '':
            lengthf = 0
        else:
            lengthf = float(length)
        dm1 = values['dm1']
        if dm1 == '':
            dm1x = 'mm'
        else:
            dm1x = dm1
        dm2 = values['dm2']
        
        if dm2 == '':
            dm2x = 'mm'
        else:
            dm2x = dm2
            
        if dm1x == 'mm':
            x1 = 1
        elif dm1x == 'cm':
            x1 = 10
        elif dm1x == 'dm':
            x1 = 100
        elif dm1x == 'm':
            x1 = 1000
        elif dm1x == 'km':
            x1 = 1000000
        elif dm1x == 'in':
            x1 = 25.4
        elif dm1x == 'ft':
            x1 = 304.8
        elif dm1x == 'yd':
            x1 = 914.4
        elif dm1x == 'mile':
            x1 = 1609340
        elif dm1x == 'NM':
            x1 = 1851995.396854
            
        if dm2x == 'mm':
            x2 = 1
        elif dm2x == 'cm':
            x2 = 10
        elif dm2x == 'dm':
            x2 = 100
        elif dm2x == 'm':
            x2 = 1000
        elif dm2x == 'km':
            x2 = 1000000
        elif dm2x == 'in':
            x2 = 25.4
        elif dm2x == 'ft':
            x2 = 304.8
        elif dm2x == 'yd':
            x2 = 914.4
        elif dm2x == 'mile':
            x2 = 1609340
        elif dm2x == 'NM':
            x2 = 1851995.396854
        
        length2 = round((lengthf * x1 / x2), 3)
        window['LENGTHCALC'].update(length2)
    
    elif event == "CONVERT AREA": # convert units of area
        area = values['area']
        if area == '':
            areaf = 0
        else:
            areaf = float(area)
        dm1 = values['dm3']
        if dm1 == '':
            dm1x = 'm2'
        else:
            dm1x = dm1
        dm2 = values['dm4']
        if dm2 == '':
            dm2x = 'm2'
        else:
            dm2x = dm2
        
        if dm1x == "m2" or dm1x == "a" or dm1x == "ha" or dm1x == "km2":
            if dm1x == "m2":
                am = 1
            elif dm1x == "a":
                am = 100
            elif dm1x == "ha":
                am = 10000
            elif dm1x == "km2":
                am = 1000000
            aream = areaf * am
            areain = aream * 1550
            if dm2x == "m2":
                area2 = aream / 1
            elif dm2x == "a":
                area2 = aream / 100
            elif dm2x == "ha":
                area2 = aream / 10000
            elif dm2x == "km2":
                area2 = aream / 1000000
            elif dm2x == "in2":
                area2 = areain / 1
            elif dm2x == "ft2":
                area2 = areain / 144
            elif dm2x == "yd2":
                area2 = areain / 1296
            elif dm2x == "arce":
                area2 = areain / 6273000
            elif dm2x == "square mile":
                area2 = areain / 4014000000
        elif dm1x == "in2" or dm1x == "ft2" or dm1x == "yd2" or dm1x == "arce" or dm1x == "square mile":
            if dm1x == "in2":
                ain = 1
            elif dm1x == "ft2":
                ain = 144
            elif dm1x == "yd2":
                ain = 1296
            elif dm1x == "arce":
                ain = 6273000
            elif dm1x == "square mile":
                ain = 4014000000
            areain = areaf * ain
            aream = areain / 1550
            if dm2x == "m2":
                area2 = aream / 1
            elif dm2x == "a":
                area2 = aream / 100
            elif dm2x == "ha":
                area2 = aream / 10000
            elif dm2x == "km2":
                area2 = aream / 1000000
            elif dm2x == "in2":
                area2 = areain / 1
            elif dm2x == "ft2":
                area2 = areain / 144
            elif dm2x == "yd2":
                area2 = areain / 1296
            elif dm2x == "arce":
                area2 = areain / 6273000
            elif dm2x == "square mile":
                area2 = areain / 4014000000
        area3 = round(area2, 3)
        window['AREACALC'].update(area3)
        
    elif event == "CONVERT SPEED": # convert units of speed
        speed = values['speed']
        if speed == '':
            speedf = 0
        else:
            speedf = float(speed)
        dm1 = values['dm5']
        if dm1 == '':
            dm1x = 'm/s'
        else:
            dm1x = dm1
        dm2 = values['dm6']
        
        if dm2 == '':
            dm2x = 'm/s'
        else:
            dm2x = dm2
        
        if dm1x == 'm/s':
            x1 = 1
        elif dm1x == 'km/h':
            x1 = 3.6
        elif dm1x == 'mph':
            x1 = 2.23694
        elif dm1x == 'kt':
            x1 = 1.94384
        elif dm1x == 'ft/s':
            x1 = 3.28084
        
        if dm2x == 'm/s':
            x2 = 1
        elif dm2x == 'km/h':
            x2 = 3.6
        elif dm2x == 'mph':
            x2 = 2.23694
        elif dm2x == 'kt':
            x2 = 1.94384
        elif dm2x == 'ft/s':
            x2 = 3.28084
        
        speed2 = round((speedf / x1 * x2), 3)
        window['SPEEDCALC'].update(speed2)
    
    elif event == "CONVERT TEMPERATURE": # convert units of temperature
        temp = values['temp']
        if temp == '':
            tempf = 0
        else:
            tempf = float(temp)
        dm1 = values['dm7']
        if dm1 == '':
            dm1x = '°C'
        else:
            dm1x = dm1
        dm2 = values['dm8']
        if dm2 == '':
            dm2x = '°C'
        else:
            dm2x = dm2
        
        if dm1x == '°C' and dm2x == 'K':
            temp2 = round((tempf + 273.15), 2)
        elif dm1x == 'K' and dm2x == '°C':
            temp2 = round((tempf - 273.15), 2)
        elif dm1x == '°C' and dm2x == '°F':
            temp2 = round (((tempf * 9/5) + 32), 2)
        elif dm1x == '°F' and dm2x == '°C':
            temp2 = round (((tempf - 32) * 5/9), 2)
        elif dm1x == 'K' and dm2x == '°F':
            temp2 = round ((((tempf - 273.15) * 9/5) + 32), 2)
        elif dm1x == '°F' and dm2x == 'K':
            temp2 = round (((tempf - 32) * 5/9 + 273.15), 2)
        else:
            temp2 = tempf
        
        window['TEMPCALC'].update(temp2)
        
    elif event == "CONVERT TIME":
        time = values['time']
        if time == '':
            timef = 0
        else:
            timef = float(time)
        dm1 = values['dm9']
        if dm1 == '':
            dm1x = 'second'
        else:
            dm1x = dm1
        dm2 = values['dm10']
        if dm2 == '':
            dm2x = 'second'
        else:
            dm2x = dm2
        
        if dm1x == 'second':
            x1 = 1
        elif dm1x == 'minute':
            x1 = 60
        elif dm1x == 'hour':
            x1 = 360
        elif dm1x == 'day':
            x1 = 8640
        elif dm1x == 'week':
            x1 = 60480
            
        if dm2x == 'second':
            x2 = 1
        elif dm2x == 'minute':
            x2 = 60
        elif dm2x == 'hour':
            x2 = 360
        elif dm2x == 'day':
            x2 = 8640
        elif dm2x == 'week':
            x2 = 60480
        
        time2 = round((timef * x1 / x2), 3)
        window['TIMECALC'].update(time2)

    elif event == "CONVERT FUEL ECONOMY":
        fuel = values['fuel']
        dm1 = values['dm11']
        dm2 = values['dm12']

        if fuel == '':
            fuelf = 0
        else:
            fuelf = float(fuel)
        
        if dm1 == '':
            dm1x = 'L/100km'
        else:
            dm1x = dm1

        if dm2 == '':
            dm2x = 'L/100km'
        else: 
            dm2x = dm2
        
        if dm1x == "L/100km":
            if dm2x == "US mpg":
                fuel2 = 235.215 / fuelf
            elif dm2x == "I mpg":
                fuel2 = 282.481 / fuelf
            else:
                fuel2 = fuelf
        elif dm1x == "US mpg":
            if dm2x == "L/100km":
                fuel2 = 235.215 / fuelf
            elif dm2x == "I mpg":
                fuel2 = fuelf * 1.201
            else:
                fuel2 = fuelf
        elif dm1x == "I mpg":
            if dm2x == "L/100km":
                fuel2 = 282.481 / fuelf
            elif dm2x == "US mpg":
                fuel2 = fuelf / 1.201
            else:
                fuel2 = fuelf
        
        fuel3 = round(fuel2, 3)
        window['FUELCALC'].update(fuel3)
        
    elif event == "CLEAR":
        window['length'].update('')
        window['dm1'].update('')
        window['dm2'].update('')
        window['LENGTHCALC'].update('')
        window['area'].update('')
        window['dm3'].update('')
        window['dm4'].update('')
        window['AREACALC'].update('')
        window['speed'].update('')
        window['dm5'].update('')
        window['dm6'].update('')
        window['SPEEDCALC'].update('')
        window['temp'].update('')
        window['dm7'].update('')
        window['dm8'].update('')
        window['TEMPCALC'].update('')
        window['time'].update('')
        window['dm9'].update('')
        window['dm10'].update('')
        window['TIMECALC'].update('')
        window['fuel'].update('')
        window['dm11'].update('')
        window['dm12'].update('')
        window['FUELCALC'].update('')
        
# to add: volume, power, pressure