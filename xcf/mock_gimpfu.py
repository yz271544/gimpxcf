# mock_gimpfu.py
class Image:
    def __init__(self, width, height, image_type):
        self.width = width
        self.height = height
        self.image_type = image_type
        self.layers = []
        self.resolution = (72, 72)

    def add_layer(self, layer, position):
        self.layers.insert(position, layer)

class Layer:
    def __init__(self, image, name, width, height, layer_type, opacity, mode):
        self.image = image
        self.name = name
        self.width = width
        self.height = height
        self.layer_type = layer_type
        self.opacity = opacity
        self.mode = mode

    def fill(self, fill_type):
        pass

class PDB:
    def gimp_context_set_background(self, color):
        pass

    def gimp_image_select_rectangle(self, img, channel_op, x, y, width, height):
        pass

    def gimp_edit_stroke(self, layer):
        pass

    def gimp_text_fontname(self, img, drawable, x, y, text, border, antialias, size, size_type, fontname):
        return Layer(img, text, 100, 50, 1, 100, 3)

    def gimp_xcf_save(self, run_mode, image, drawable, filename, raw_filename):
        pass

    def gimp_displays_flush(self):
        pass

gimp = Image
pdb = PDB()
RGB = 0
RGB_IMAGE = 1
BACKGROUND_FILL = 0
CHANNEL_OP_REPLACE = 0
NORMAL_MODE = 3