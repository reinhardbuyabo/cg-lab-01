import cairo

def create_surface(width, height, background_color):
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)
    context.set_source_rgb(*background_color)
    context.paint()

    return surface, context

def write_to_surface(surface, filename):
    surface.write_to_png(filename)