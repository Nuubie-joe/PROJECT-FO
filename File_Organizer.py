#step 1
import os
import shutil

#step 5 

document = 0
videos = 0
text = 0
images = 0

#step 2
file_path = input("Enter a File path: ")

#step 3
if os.path.exists(file_path):
    print("The file exists!")
else:
    print("doesn't exist")


#step 4
list_of_files = os.listdir("C:/Users/STUDENTS/Desktop/Test_Montes_Danielle")
print(list_of_files)




if os.path.exists('finals.pdf'):
    print("subfolders exist")
else:
    print("doesn't exist")




