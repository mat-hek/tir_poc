import os
import re
import time

import variables


def get_temperature():
    temp = os.popen("cat /sys/class/hwmon/hwmon0/temp1_input").read().strip()
    return int(temp)


def get_is_charging():
    state = os.popen("upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep state").read().strip()
    if "discharging" in state: 
        return 0 
    else:
        return 1


while True:
    temp = get_temperature()
    is_charging = get_is_charging()
    print("temp: {}, is charging: {}".format(temp, is_charging))
    variables.temp.save_value({'value': temp})
    variables.is_charging.save_value({'value': is_charging})

    time.sleep(5)
