from pynput.keyboard import Key, Events

from grid import GridWalker, Direction
from pynput import keyboard


def main():
    grid_walker = GridWalker()

    grid_walker.print_grid()
    while True:
        with keyboard.Events() as events:
            event = events.get()
            if isinstance(event, Events.Press):
                if event.key == Key.up:
                    grid_walker.move_and_print(Direction.UP)
                elif event.key == Key.down:
                    grid_walker.move_and_print(Direction.DOWN)
                elif event.key == Key.left:
                    grid_walker.move_and_print(Direction.LEFT)
                elif event.key == Key.right:
                    grid_walker.move_and_print(Direction.RIGHT)


if __name__ == '__main__':
    main()
