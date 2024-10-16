import cairo

def create_surface(width, height, background_color):
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)
    context.set_source_rgb(*background_color)
    context.paint()

    return surface, context

def house(context, color, line_width):
    context.set_source_rgb(*color)
    context.set_line_width(line_width)
    context.move_to(100, 100)
    context.line_to(100, 150)
    context.line_to(150, 150)
    context.line_to(150, 300)
    context.line_to(450, 300)
    context.line_to(450, 150)
    context.stroke()
    

def write_to_surface(surface, filename):
    surface.write_to_png(filename)