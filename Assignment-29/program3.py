"""3. Write a Python script to read the above created file ‘myfile.txt’ and display content on
the console."""

f=open("myfile.txt","w")
f.write("hello i m mohit sahu \n i want to do something in any way and also excited to find a respected job")
f.write("\n----------------*-------------------------------")
print("massg are stored in file successfully")
f.close()



f=open("myfile.txt","r")
call=f.read()
print(call)
print("massg are print in console ")
f.close()