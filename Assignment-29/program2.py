#2. Write a Python script to create a new file ‘myfile.txt’ and store user entered text.

import os
f=open("myfile.txt","w")
f.write(input("Enter text which you any type here ..:"))
print("user entered mssg successfully")
f.close()


# find the file name
find_path="C:\\Users\Subhash kumar\Documents\\Assignment-29\\myfile.txt"
find_file_name=os.path.basename(find_path)
print(find_file_name)
