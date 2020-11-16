import re
import csv

def goodbye():
    print('Thank you for checking in today!')

rating = input('What is your rating for this day on a scale of 1-10? ')

while re.match(r'^\d{1,10}', rating):
    rating = input("Please enter a number 1-10. ")
    break

    

#try:
    #re.match(r'^\d{1-10}', rating)


goodbye()


#while rating == re.match('[1-10]', rating):


        #while True:
            #if int(rating) >0 & <11:
                #break
              #print("Please enter a number between 1-10")