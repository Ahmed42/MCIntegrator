
import integrator
import visualizer
import math
import argparse

def find_max_y(func_expr, x_min, x_max, delta):
    max_y = -math.inf
    for x in range(int(x_min * 10), int(x_max * 10), int(delta * 10)):
        x /= 10
        y = eval(func_expr, {}, {'x': x})
        if y > max_y:
            max_y = y
    return max_y

def find_min_y(func_expr, x_min, x_max, delta):
    min_y = math.inf
    for x in range(int(x_min * 10), int(x_max * 10), int(delta * 10)):
        x /= 10
        y = eval(func_expr, {}, {'x': x})
        if y < min_y:
            min_y = y
    return min_y 

if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("func_expr", type=str, help="Integrand function expression")
    args_parser.add_argument("from_limit", type=float, help="Lower limit")
    args_parser.add_argument("to_limit", type=float, help="Upper limit")

    args = args_parser.parse_args()

    func_expr = args.func_expr
    x_min = args.from_limit
    x_max = args.to_limit


    delta_x = 0.1
    y_max = find_max_y(func_expr, x_min, x_max, delta_x)
    y_min = find_min_y(func_expr, x_min, x_max, delta_x)
    total_points_count = 1000

    result, xs, ys, points_types = integrator.integrate(func_expr, x_min, x_max, y_min, y_max, total_points_count)
    print("Result: ", result)

    anim = visualizer.run_animation(func_expr, xs, ys, points_types, x_min, x_max, y_min, y_max, delta_x)

