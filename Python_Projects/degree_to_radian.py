# a function that will convert degree to radian! 
"""
    #180 = pi rad
    1 deg = pi/180
    
    1 rad = 180/ pi 
"""
    

def radians_to_degrees(degrees: int) -> float:
    
    return round(degrees*(180/(22/7)),1)

print(radians_to_degrees(20))
