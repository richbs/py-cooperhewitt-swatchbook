import importlib

def load_palette(reference):
    pkg = "cooperhewitt.swatchbook.%s" % reference
    mod = importlib.import_module(pkg)
    return mod.palette()

def closest(reference, hex):
    palette = load_palette(reference)
    return palette.closest(hex)

def closest_delta_e(reference, hex):
    palette = load_palette(reference)
    return palette.closest_delta_e(hex)


if __name__ == '__main__':

    import sys

    ref = sys.argv[1]
    hex = sys.argv[2]

    p = load_palette(ref)

    print(p.sorted())

    print(p.closest(hex))
    print(p.closest_delta_e(hex))
