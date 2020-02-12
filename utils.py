from PIL import Image
import os


def get_cropped_image(im_orig, left=725, top=15, right=1325, bottom=715):
    cropped = im.crop((left, top, right, bottom))
    return cropped


def generate_croppes():
    """function to crop all images  in screenshots_path
    """
    crops_path = "./images/crops/"
    screenshots_path = "./images/screenshots/"
    list_screenshots = os.listdir(screenshots_path)
    for i, file in enumerate(list_screenshots):
        if i % 100 == 0:
            print("cropping image", i)
        im = Image.open(screenshots_path+file)
        im2 = get_cropped_image(im)
        im2.save(crops_path+"cropped_"+file)
