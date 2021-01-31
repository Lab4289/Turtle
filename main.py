# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import sys
import math
from Turtle_Activity import turtle,yoke

latitude = 19.99
longitude = 73.78
file_n = 'random_lat_lon.txt'
file_log='Log_turtle.log'

def generate_random_data(lat, lon, num_rows, file_name):
    with open(file_name, 'w') as output:
        for _ in range(num_rows):
            hex1 = '%012x' % random.randrange(16**12)
            flt = float(random.randint(0,100))
            dec_lat = random.random()/100
            dec_lon = random.random()/100
            output.write('%s %.1f %.6f %.6f \n' % (hex1.lower(), flt, lon+dec_lon, lat+dec_lat))

def Log(text,file_name):
    with open(file_name, 'a') as output:
        output.write('%s \n' %(text))
        output.close()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    #generate_random_data(latitude, longitude, 5, file_n)
    for _ in range(500):
        hex1 = '%012x' % random.randrange(16 ** 12)
        seq=str(hex1.lower())+","+str(_+1)+","
        t=seq+turtle()
        y=seq+yoke()
        Turlog=str(t)+"\n"+str(y)
        Log(Turlog, file_log)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
