import os
import re
import time

import variables


def get_battery_info(name):
    output = os.popen("ioreg -rn AppleSmartBattery | grep {}".format(name)).read().strip()
    return re.fullmatch('\"{}\" = (.*)'.format(name), output).group(1)


def get_temperature():
    return float(get_battery_info("Temperature"))/100


def get_is_charging():
    return get_battery_info("IsCharging") == "Yes"


while True:
    temp = get_temperature()
    is_charging = get_is_charging()
    print("temp: {}, is charging: {}".format(temp, is_charging))
    variables.temp.save_value({'value': temp})
    variables.is_charging.save_value({'value': is_charging})

    time.sleep(1)
