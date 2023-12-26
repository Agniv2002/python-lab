import math
def distance(x1,x2,y1,y2):
    return math.sqrt((x1-x2)**2 - (y1-y2)**2);

def cost(units):
    if(units<200):
        return units*500
    elif (units<600):
        return units*1000
    else:
        return units*400
    
x1=int(input("enter the value of x1"))
x2=int(input("enter the value of x2"))
y1=int(input("enter the value of y1"))
y2=int(input("enter the value of y2"))
print(f'the distance is{distance(x1,x2,y1,y2)}')
units =int(input("Enter the cost"))
print(f'the cost is {cost(units)}')
