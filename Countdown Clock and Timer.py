#Countdown Clock and Timer

import time

countdown = int(input("Countdown Time in Seconds? - "))

for n in range(countdown):
    time.sleep(1)
    print(countdown)
    countdown = countdown - 1


#test
#Countdown Time in Seconds? - -10

#Countdown Time in Seconds? - 10
#10
#9
#8
#7
#6
#5
#4
#3
#2
#1

#Countdown Time in Seconds? - 05
#5
#4
#3
#2
#1
    
    
