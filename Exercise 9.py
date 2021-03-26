# Oh Soldier Prettify My Folder

import os

def soldier(path,ext):
    files = os.listdir(path)
    os.chdir(path)

    for file in files:
        os.rename(file,file.title())

    # for index, file in enumerate(files):
    #     os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))

    i = 1
    for file2 in files:
        filename, file_extension = os.path.splitext(file2)
        if file_extension == ext:
            new_name =str(i)+ file_extension
            os.rename(file2,new_name)
            i = i + 1




path ='F:/xyz'
ext = ".Jpg"

soldier(path,ext)