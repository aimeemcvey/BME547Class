# line_coordinates.py


def point_input():
    point1 = input("Insert point 1 (x1, y1): ")
    point2 = input("Insert point 2 (x2, y2): ")
    point1_info = point1.split(",")
    point2_info = point2.split(",")
    point_input.x1, point_input.y1 = float(point1_info[0]), float(point1_info[1])
    #point1 = (x1, y1)
    point_input.x2, point_input.y2 = float(point2_info[0]), float(point2_info[1])
    #point2 = (x2, y2)
    return point_input.x1, point_input.y1, point_input.x2, point_input.y2


def new_point_calc(x1, y1, x2, y2):
    m = (y2-y1)/(x2-x1)
    new_point_calc.m = m
    new_point_calc.y0 = y1 + m*(0-x1)
    return new_point_calc.m, new_point_calc.y0


def new_pair(m, y0):
    new_x = float(input("Give me another x: "))
    new_y = m*new_x + y0
    print("Your y for a point on this line is {}." .format(new_y))


if __name__ == "__main__":
    point_input()
    new_point_calc(point_input.x1, point_input.y1, point_input.x2, point_input.y2)
    new_pair(new_point_calc.m, new_point_calc.y0)
