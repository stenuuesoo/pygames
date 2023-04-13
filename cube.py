import curses

def main(stdscr):
    # Set up the terminal
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.clear()
    stdscr.refresh()

    # Initialize colors
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(curses.COLOR_CYAN, curses.COLOR_CYAN, -1)

    # Set up the cube
    cube = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 1],
        [1, 1, 1],
        [1, 0, 1]
    ]
    cube_color = curses.COLOR_CYAN
    x, y, z = 0, 0, 0
    dx, dy, dz = 1, 1, 1

    # Move the cube
    while True:
        # Clear the screen
        stdscr.clear()

        # Draw the cube
        for i, (px, py, pz) in enumerate(cube):
            x_pos = int(px + x)
            y_pos = int(py + y)
            z_pos = int(pz + z)

            if x_pos >= curses.COLS or y_pos >= curses.LINES:
                continue

            char = chr(ord('a') + i)
            stdscr.addch(y_pos, x_pos, char, curses.color_pair(cube_color))

        # Move the cube
        x += dx
        y += dy
        z += dz

        if x <= 0 or x + 1 >= curses.COLS:
            dx = -dx
        if y <= 0 or y + 1 >= curses.LINES:
            dy = -dy
        if z <= 0 or z + 1 >= 3:
            dz = -dz

        # Refresh the screen
        stdscr.refresh()

        # Wait a bit before updating the screen again
        curses.napms(50)

if __name__ == '__main__':
    curses.wrapper(main)