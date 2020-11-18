import csv


#from matplotlib import pyplot as plt

filename = 'users.csv'

#create function to read csv file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

#if you wanted to see each index and data for header column
    #for index, column_header in enumerate(header_row):
        #print(index, column_header)




#create ratings list to store data from each row
    ratings = []
    for row in reader:
        #append daily rating from each row
        ratings.append(row[5])  
    print(ratings)



#convert strings to int and ignore empty strings
#for row in reader:
    #if row[5] == '':        #if empty string, continue itteratin
        #continue
    #rating = int(row[5])   #change string to int
    #ratings.append(rating)       #add rating to ratings list

#print(ratings)