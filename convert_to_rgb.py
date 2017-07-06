rgb_background = {"r":255,"g":255,'b':255}
rgba_color = {"r":30,"g":188,'b':191,'a':0.43}
def convert_rgba_to_exa(rgb_background,rgba_color):
    alpha = rgba_color['a']
    new_rgb = {}
    for i,v in rgb_background.iteritems():
        new_rgb[i] = int((1 - alpha) * rgb_background[i] + alpha * rgba_color[i])
    return new_rgb
print convert_rgba_to_exa(rgb_background,rgba_color)
