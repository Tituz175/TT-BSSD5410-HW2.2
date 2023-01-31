from SortFunctions import quickSortIterative
from SearchFunctions import binarySearch_sub
from PixelFunctions import storePixels, pixels_to_image, compare_pixels, pixels_to_points, grayscale
from PIL import Image


def main():
    threshold = int(input("Kindly enter your desired threshold: "))
    IMG_NAME = "monkey"

    with Image.open(IMG_NAME + ".jpg") as im:
        pixels = storePixels(im)
        print("stored")
        sorted_pixels = pixels.copy()
        quickSortIterative(sorted_pixels, 0, len(sorted_pixels) - 1, compare_pixels)
        print("sorted")
        subi = binarySearch_sub([r[0][0] for r in sorted_pixels], 0, len(sorted_pixels) - 1, threshold)
        print("Sublist of reds starts at: ", subi)
        grayscale(im, pixels)
        pixels_to_points(im, sorted_pixels[subi:])

    # save my image data from memory to a file with a different name
    im.save("highlighted_" + IMG_NAME + ".jpg", "JPEG")


# end def main():


if __name__ == "__main__":
    main()
