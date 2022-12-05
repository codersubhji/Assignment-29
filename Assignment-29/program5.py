#5. Write a Python script to append list of city names in a file ‘cities.txt’

append_me="\nfatehpur"
app=open("cities.txt",'a')
use=app.write(append_me)
print("successful append")
app.close()
