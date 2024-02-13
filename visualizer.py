import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import functools

def generate_points(func_expr, x_min, x_max, delta):
    xs = [x/10.0 for x in range(int(x_min * 10), int(x_max * 10), int(delta * 10))]
    ys = [eval(func_expr, {}, {'x' : x}) for x in xs]
    return xs, ys

def update_animation(frame, scatt, xs = [], ys = [], colors = []):
    scatt.set_color(colors[:frame])
    data = np.stack([xs[:frame], ys[:frame]]).T
    scatt.set_offsets(data)
    return scatt

def run_animation(func_expr, xs, ys, points_types, x_min, x_max, y_min, y_max, delta_x):
    colors = []
    for point_type in points_types:
        color = ''
        if point_type == 1:
            color = 'green'
        elif point_type == -1:
            color = 'red'
        else:
            color = 'black'
        colors.append(color)

    plot_xs, plot_ys = generate_points(func_expr, x_min, x_max, delta_x)
    fig, ax = plt.subplots()
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    ax.plot(plot_xs, plot_ys)
    ax.set(xlim=(x_min, x_max), ylim=(y_min, y_max))
    ax.axis('on')
    scatt = ax.scatter([], [])

    anim = animation.FuncAnimation(fig, functools.partial(update_animation, scatt = scatt, xs = xs, ys = ys, colors = colors), frames=len(xs), interval=1)
    plt.show()
    return anim
