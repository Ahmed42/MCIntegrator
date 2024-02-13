import random

def point_within(func_expr, point):
    x, y = point
    function_y = eval(func_expr, {}, {'x': x})
    if function_y < 0 and y < 0 and y >= function_y:
        return -1
    elif function_y > 0 and y > 0 and y <= function_y:
        return 1
    else:
        return 0

def integrate(func_expr, x_min, x_max, y_min, y_max, total_points_count):
    count = 0

    xs = [] 
    ys = []
    points_types = []
    for _ in range(total_points_count):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        point_type= point_within(func_expr, (x, y))
        count += point_type

        xs.append(x)
        ys.append(y)
        points_types.append(point_type)

    square_area = (y_max - y_min) * (x_max - x_min)

    result = (count/total_points_count) * square_area
    return result, xs, ys, points_types

# TODO a 'func' object that holds y_min, y_max, from parsing a func_expr
