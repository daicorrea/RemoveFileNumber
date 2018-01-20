import os

def rename_files():
    #(1) get file names from folder
    file_list = os.listdir('./prank')
    #print file list
    print(file_list)
    #change current working directory to rename files
    os.chdir('./prank')
    #(2) Rename files in a loop
    for file_name in file_list:
        #Using the translate function to remove numbers
        os.rename(file_name, file_name.translate(None, '0123456789'))


rename_files()