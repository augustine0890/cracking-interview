"""
Given time in hh:mm format, caculate the shorter angle between the hour and minute hand in an analog clock.
(hh:60 should be considered as (hh+1):0)
Degree(hr) = (360/12)*hours + (360/12)/(60/mins)
Degree(min) = (360/60)*mins
"""

def findAngle(hours, mins):
    if (mins == 60):
        hours += 1
        mins = 0
    
    if mins == 0:
        minAngle = 0
        hourAngle = hours*30
    else:
        minAngle = mins*6
        hourAngle = hours*30 + 30/(60/mins)

    if abs(minAngle-hourAngle) > 180:
        return round(360 - abs(minAngle-hourAngle),2)
    else:
        return round(abs(minAngle-hourAngle),2)

test1 = findAngle(3, 5)
print(test1)
test2 = findAngle(3, 60)
print(test2)
test3 = findAngle(5, 30)
print(test3)
test4 = findAngle(9, 00)
print(test4)
test5 = findAngle(12, 00)
print(test5)
