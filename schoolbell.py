#!/usr/bin/python3

# Simple python script to play sounds over the school day
# Credit to https://gist.github.com/BillSimpson/d7a1a531995c8b63492bb47ef8872618

belltones = {
    'warn' : 'quick_chime.wav',
    'start' : 'slow_chime.wav',
    'back' : 's1bell.wav',
    'end' : 'divinebell.wav',
    'bus' : 'jimmy1.wav'
}

bellschedule = {   
    '08:49' : 'warn',
    '08:50' : 'back',   
    '09:39' : 'warn',
    '09:40' : 'start',
    '10:29' : 'warn',
    '10:30' : 'end',
    '10:44' : 'warn',
    '10:45' : 'back',    
    '11:34' : 'warn',
    '11:35' : 'start',
    '12:24' : 'warn',
    '12:25' : 'start',
    '13:14' : 'warn',
    '13:15' : 'end',
    '14:09' : 'warn',
    '14:10' : 'back',
    '14:59' : 'warn',
    '15:00' : 'start',
    '15:49' : 'warn',
    '15:50' : 'end',
    '16:05' : 'bus',
}

# # dictionary for testing
# bellschedule = {   
#     '17:41' : 'start',
#     '17:42' : 'start',   
#     '17:43' : 'start',
#     '17:44' : 'start',
#     '17:45' : 'start'
# }

holidays = {
    '2020-09-07',
    '2020-09-25',
}

from datetime import datetime
from time import sleep
from pygame import mixer

# Remove stuttering effect (see pygame.mixer.Sound.play issue #322
mixer.pre_init(buffer=2048)
# Initialise mixer
mixer.init()

filename = None

dt = datetime.now()

# Store time
timestr = dt.strftime('%H:%M')
# Store date
datestr = dt.strftime('%Y-%m-%d')

# Check if Mon - Fri and not in holidays
if dt.weekday() < 5 and datestr not in holidays:  
    
    # it is a weekday not a holiday, do chimes
    print('It is a schoolday, checking time '+timestr)

    if timestr in bellschedule:
        
        # Change filename using belltones dictionary
        filename = belltones[bellschedule[timestr]]
        
        # Print name of file
        print(filename)

else:
    
    # print holiday message
    print('It is a weekend or holiday -- enjoy!')

if filename:
    
    # Print ring bell
    print("Ring bell")
    
    # Load in sound
    mixer.music.load(filename)
    # Play sound
    mixer.music.play()
    
    # Sleep 20 seconds to allow sounds to play
    # Note - No sound played without sleep command!
    sleep(20)
