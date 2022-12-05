"""6. Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or
not"""

fh=open("city.txt",'w')
fh.write("""Agra
Aligarh
Amroha
Ayodhya
Azamgarh
Bahraich
Ballia
Banda
Bara Banki
Bareilly
Basti
Bijnor
Bithur
Budaun
Bulandshahr
Deoria
Etah
Etawah
Faizabad
Farrukhabad-cum-Fatehgarh
Fatehpur
Fatehpur Sikri
Ghaziabad
Ghazipur
Gonda
Gorakhpur
Hamirpur
Hardoi
Hathras
Jalaun
Jaunpur
Jhansi
Kannauj
Kanpur
Lakhimpur
Lalitpur
Lucknow
Mainpuri
Mathura
Meerut
Mirzapur-Vindhyachal
Moradabad
Muzaffarnagar
Partapgarh
Pilibhit
Prayagraj
Rae Bareli
Rampur
Saharanpur
Sambhal
Shahjahanpur
Sitapur
Sultanpur
Tehri
Varanasi""")
print("file successful create")
fh.close()


fh=open("city.txt",'r')
word=input("Enter any city which is exits on uttar pradesh:")
s=" "
count=1
while s:
    s=fh.readline()
    L=s.split()
    if word in L:
        print("line number :",count ,":", s)
    count +=1 
         
     
    

fh.close()