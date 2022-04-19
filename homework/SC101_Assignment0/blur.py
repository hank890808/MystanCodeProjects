"""
File: blur.py
Name: 蕭承瀚 Hank
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    To blur the origin image by getting the average RGB
    of surrounding pixels.
    :param img: SimpleImage, the origin image
    :return: the image has been blurred
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            new_p = new_img.get_pixel(x, y)
            total_red = 0
            total_green = 0
            total_blue = 0
            n = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x + i < img.width and 0 <= y + j < img.height:
                        # To ensure the neighbors exist in origin image.
                        total_p = img.get_pixel(x + i, y + j)
                        total_red += total_p.red
                        total_green += total_p.green
                        total_blue += total_p.blue
                        # Calculate the sum of nearest neighbors R, G, B separately.
                        n += 1
                        # n represents how many neighbors there are.
            new_p.red = total_red // n
            new_p.green = total_green // n
            new_p.blue = total_blue // n
    return new_img


def main():
    """
    This program will blur the origin image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
