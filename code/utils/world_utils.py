def get_neighbors(grid, x, y):
    neighbors = {
        'top': grid[y-1][x] if y > 0 else None,
        'left': grid[y][x-1] if x > 0 else None,
        'bottom': grid[y+1][x] if y < len(grid) - 1 else None,
        'right': grid[y][x+1] if x < len(grid) - 1 else None,
        'top_left': grid[y-1][x-1] if x > 0 and y > 0 else None,
        'top_right': grid[y-1][x+1] if x < len(grid) - 1 and y > 0 else None,
        'bottom_right': grid[y+1][x+1] if x < len(grid) - 1 and y < len(grid) - 1 else None,
        'bottom_left': grid[y+1][x-1] if x > 0 and y < len(grid) - 1 else None
    }

    return neighbors