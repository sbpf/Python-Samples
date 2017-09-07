import os

def rename_files():
    #Get file names from a folder
    filenames_list = os.listdir(r"E:\NanoDegree\Part1\02SecretMessage\assignment")
    saved_path=os.getcwd()
    os.chdir(r"E:\NanoDegree\Part1\02SecretMessage\assignment")       
     
    #rename each filename that has number
    for file_name in filenames_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))

    os.chdir(saved_path)

rename_files()
