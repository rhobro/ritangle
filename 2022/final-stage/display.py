from matplotlib import pyplot as plt


def show_it(mountains, path=None):
    # draw grid
    grid = flatten([
        [
            (i, j)
            for j in range(30)
            if i**2 + j**2 < 784
        ]
        for i in range(30)
    ])
    grid_xs = [a for a, _ in grid]
    grid_ys = [b for _, b in grid]
    plt.scatter(grid_xs, grid_ys, marker="o", s=3)
    
    # spot mountains
    mountain_xs = [m.coords[0] for m in mountains]
    mountain_ys = [m.coords[1] for m in mountains]
    plt.scatter(mountain_xs, mountain_ys, marker="o", s=25)
    
    # plot path
    if path is not None:
        path_xs = [p[0] for p in path]
        path_ys = [p[1] for p in path]
        plt.plot(path_xs, path_ys)
    
    plt.gca().set_aspect("equal")
    plt.show()

def force_aspect(fig,aspect=1):
    xsize,ysize = fig.get_size_inches()
    minsize = min(xsize,ysize)
    xlim = .4*minsize/xsize
    ylim = .4*minsize/ysize
    if aspect < 1:
        xlim *= aspect
    else:
        ylim /= aspect
    fig.subplots_adjust(left=.5-xlim,
                        right=.5+xlim,
                        bottom=.5-ylim,
                        top=.5+ylim)
    
# util
def flatten(src):
    flattened = []
    for element in src:
        if type(element) is list:
            for item in element:
                flattened.append(item)
        else:
            flattened.append(element)
    return flattened