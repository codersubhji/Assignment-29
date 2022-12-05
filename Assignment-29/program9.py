"""9. Write a Python script to store book data in a file. Book data is in the form of a
dictionary in which book name is the key and price is its value. Use pickle to store
data into a file (say bookfile)"""

#without usig of pickle method

# class books:
#     def __init__(self,book_name,book_price):
#         self.book_name=book_name
#         self.book_price=book_price
    
#     def create_book_data(self):
#         file1=open("file1.txt",'w')
#         file2= self.book_price
#         file1.write(self.book_name)
#         file1.write(file2) 
       
#         print("file are create successfully")
#         file1.close()
    
 
        
        
# obj=books("Mathematics", " : 1100")     
# obj.create_book_data()   
          
          
      # by using of pickle mehtod create a file as a dicstionary

import pickle

book_dics={"English:400","Hindi:300","Science:800","Social Science:600","Math:1000","Physics:400","Chemestry:1100"}          
with open("book_file.pkl",'wb') as book:
    pickle.dump(book_dics, book)
print("successful") 

with open("book_file.pkl",'rb') as book:
    call=pickle.load(book) 
print(call)      
print("print again succesful")

