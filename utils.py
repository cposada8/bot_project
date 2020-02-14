from PIL import Image
import os
import pandas as pd


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

def create_database(file_name, path_to_save, columns):
    """this function creates a database .csv file
    it will have the name 
    
    Parameters
    ----------
    file_name : str
        the name to save the file
    path_to_save: str
        the path where the file is going to be saved
    columns : list of str
        a list of the columns in the dataframe
    """
    df = pd.DataFrame(columns=columns)
    df.to_csv(path_to_save+file_name, sep=";", index=False)


def database_init():
    """This method will create an empty database and
    save it as csv in a folder
    """
    path_to_save = "./databases/"
    file_name = "database.csv"
    columns = ["image_name", "user", "rank", "date"]
    
    df = pd.DataFrame(columns=columns)
    df.to_csv(path_to_save+file_name, sep=";", index=False)


def save_register(df, register):
    """this function takes a df and a register and returns
    the same df but with the register in the last row
    Note: this function will change the df inplace
    
    Parameters
    ----------
    df : Pandas DataFrame
        df to be updated
    register : Pandas DataFrame
        a register to be added to the original df
    """
    df = df.append(register)
    # return df