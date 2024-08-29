#!/usr/bin/python3
""" find perimeter of island """

bound_1 = set()
bound_2 = set()
bound_3 = set()
bound_4 = set()


def boundary(grid, i, j):
    """boundary function"""
    bounds = 0
    try:
        if i == 0:
            bounds += 1
        elif grid[i-1][j] == 0:
            bounds += 1
    except:
        bounds += 1
    try:
        if grid[i+1][j] == 0:
            bounds += 1
    except:
        bounds += 1
    try:
        if grid[i][j+1] == 0:
            bounds += 1
    except:
        bounds += 1
    try:
        if j == 0:
            bounds += 1
        elif grid[i][j-1] == 0:
            bounds += 1
    except:
        bounds += 1

    if bounds == 1:
        bound_1.add((i, j))
    elif bounds == 2:
        bound_2.add((i, j))
    elif bounds == 3:
        bound_3.add((i, j))
    elif bounds == 4:
        bound_4.add((i, j))


def island_perimeter(grid):
    """ island perimeter """
    if grid == []:
        return 0
    l = len(grid)
    w = len(grid[0])
    for i in range(l):
        for j in range(w):
            if grid[i][j] == 1:
                boundary(grid, i, j)
                if len(bound_4) != 0:
                    return 4
    perimeter = (len(bound_3) * 3) + (len(bound_2) * 2) + (len(bound_1))
    return perimeter
