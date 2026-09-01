from PIL import Image, ImageDraw

EMBER = (217, 88, 31)
GOLD = (165, 114, 10)
INK = (26, 17, 8)

def gradient_bg(size, radius):
    img = Image.new("RGB", (size, size), EMBER)
    px = img.load()
    for y in range(size):
        for x in range(size):
            t = (x + y) / (2 * size)
            r = int(EMBER[0] + (GOLD[0] - EMBER[0]) * t)
            g = int(EMBER[1] + (GOLD[1] - EMBER[1]) * t)
            b = int(EMBER[2] + (GOLD[2] - EMBER[2]) * t)
            px[x, y] = (r, g, b)
    mask = Image.new("L", (size, size), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out

def draw_mark(img, size, scale=0.52):
    d = ImageDraw.Draw(img)
    s = size * scale
    cx, cy = size / 2, size / 2
    x0, x1 = cx - s / 2, cx + s / 2
    w = max(2, int(size * 0.045))
    bar_h = s * 0.34
    plate_h = s
    # horizontal bar
    d.rounded_rectangle([x0 + s * 0.18, cy - w / 2, x1 - s * 0.18, cy + w / 2], radius=w / 2, fill=INK)
    # left plate pair
    for off in (0.0, 0.12):
        lx = x0 + s * off
        d.rounded_rectangle([lx, cy - plate_h / 2, lx + w * 1.15, cy + plate_h / 2], radius=w / 2, fill=INK)
    # right plate pair
    for off in (0.0, 0.12):
        rx = x1 - s * off - w * 1.15
        d.rounded_rectangle([rx, cy - plate_h / 2, rx + w * 1.15, cy + plate_h / 2], radius=w / 2, fill=INK)
    return img

def make(path, size, radius_ratio, scale):
    img = gradient_bg(size, int(size * radius_ratio))
    draw_mark(img, size, scale)
    img.save(path)

make("icons/icon-192.png", 192, 0.22, 0.52)
make("icons/icon-512.png", 512, 0.22, 0.52)
make("icons/icon-maskable-512.png", 512, 0.0, 0.34)  # full-bleed, safe-zone padding for maskable
make("icons/apple-touch-icon.png", 180, 0.22, 0.5)

print("done")
