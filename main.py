from functions import *

if __name__ == '__main__':
    # print('Hello, World!')
    surface, context = create_surface(600, 400, (0.8, 0.8, 0.8))

    house(context, (0, 0, 1), 2)

    write_to_surface(surface, 'output.png')
