import random as rd
from math import ceil
from time import sleep
from global_land_mask import globe
#####################################################################
def Latitude():
    Clock=round(rd.uniform(-89,89))
    Minute=round(rd.uniform(0,59),2)/60
    Second=round(rd.uniform(0,3599),2)/3600
    X=Clock+Minute+Second
    return X
#################
def Longtitude():
    Clock=round(rd.uniform(-179,179))
    Minute=round(rd.uniform(0,59),2)/60
    Second=round(rd.uniform(0,3599),2)/3600
    Y=Clock+Minute+Second
    return Y
#####################################################################
def turtle():
    while True:
        x = Latitude()
        if x>90:
            x=90
        y = Longtitude()
        if y>180:
            y=180
        globe_land_mask = globe.is_land(x,y)
        if globe_land_mask==False:
            break

    turtle="turtle,"+str(x)+","+str(y)
    return turtle
#####################################################################
def yoke():
    while True:
        x = Latitude()
        if x>90:
            x=90
        y = Longtitude()
        if y>180:
            y=180
        globe_land_mask=globe.is_land(x,y)
        if globe_land_mask==False:
            break

    yoke="yoke,"+str(x)+","+str(y)
    return yoke
#####################################################################
#print("Random float number between 10 and 100 is ", rd.uniform(10, 100))
#print("Random float number between 25.5 and 250 is ", rd.uniform(25.5, 250))
#print("Random float number between 250 and 25.5 is ", rd.uniform(250, 25.5))
#globe_land_mask = globe.is_land(-42.13718611111111, 54.26108055555555)
#print(globe_land_mask)
#for _ in range(3):
#    t=turtle()
#    y=yoke()
#    print(t)
#    print(y)