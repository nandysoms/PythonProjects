import os, zipfile


folder_path = r'C:\Users\Reshmi\Downloads\Bucky Roberts Source Code'
os.chdir(folder_path)

for item in os.listdir(folder_path):
    if zipfile.is_zipfile(os.path.abspath(item)):
        zipobj = zipfile.ZipFile(os.path.abspath(item))
        zipobj.extractall(folder_path)