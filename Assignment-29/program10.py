"""10. Write a Python script to extract book data from a bookfile using pickle. Also print
extracted book data."""

import pickle

with open("book_file.pkl",'rb') as bookfile:
    call=pickle.load(bookfile)
print(call)
    
    