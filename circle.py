from math import pi

def circle_area(radius):
    if type(radius) not in [int, float]:
        raise TypeError("Радиус должен быть неотрицательным вещественным числом на")
    #if radius < 0:
        #raise ValueError("Радиус не может быть отрицательным")
    return pi*radius**2


#r_list = [2, 0, -3, 2 + 3j, True, [2], 'seven']
#message = 'Площадь окружности с радиусом {radius} --> {area}'
#
#for r in r_list:
#    s = circle_area(r)
 #   print(message.format(radius = r, area = s))

