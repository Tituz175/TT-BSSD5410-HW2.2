from PIL import Image, ImageDraw


def compare_pixels(px1, px2):
    return px1[0][0] <= px2[0][0]


# end def compare_pixels(pix1, pix2):

def storePixels(im):
    width = int(im.size[0])
    height = int(im.size[1])

    # store pixels in a list
    pixel_array = []
    for j in range(height):
        for i in range(width):
            r, g, b = im.getpixel((i, j))
            pixel_array.append([(r, g, b), (i, j)])
        # end for j
    # end for i
    return pixel_array


# end def storePixels(im):

def pixels_to_image(im, pixels):
    outimg = Image.new("RGB", im.size)
    outimg.putdata([p[0] for p in pixels])
    outimg.show()
    return outimg


# end def pixels_to_image(im, pixels):

def pixels_to_points(im, pixels):
    for p in pixels:
        im.putpixel(p[1], p[0])
    im.show()


# end def pixels_to_points(size, pixels):

def grayscale(im, pixels):
    draw = ImageDraw.Draw(im)
    for px in pixels:
        gray_av = int((px[0][0] + px[0][1] + px[0][2]) / 3)
        draw.point(px[1], (gray_av, gray_av, gray_av))

# end def grayscale(im, pixels):
