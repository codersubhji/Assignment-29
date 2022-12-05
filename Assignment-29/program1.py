"""1. Write a Python script to print the following status of a file:
a. Whether a file is read only
b. Whether a file is closed or not
c. Which file opening mode is used
d. Name of the file"""

import os
 
f=open("file.text","w")
f.write("hello i m subhash \n")
f.write("here i m a fresher student")
print("file write successfully")
f.close()

#a. whether a file is reade only
f=open("file.text","r")
f.read()
print("file read successfully")
f.close()

#b. wether a file is closed or not (by defalut without closing file are readable) 
f=open("file.text","r")
f.read()


#c. wether file used in opening mode
f=open("file.text")
print("fiel in open mode ")


#d. Name of the file


f_p="C:\\Users\Subhash kumar\Documents\\Assignment-29\\file.text"
f_n=os.path.basename(f_p)
print(f_n)



