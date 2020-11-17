import re
import csv

def goodbye():
    print('Thank you for checking in today!')


#use regex to check rating
answer = True
while answer == True:
    rating = input('What is your rating for this day on a scale of 1-10? ')

    if not re.match(r'\b([1-9]|10)\b', rating):
        print('Error. Please follow directions. ')
        answer = True
    else:
        print('Your rating is: ' + rating)
        answer = False

        #rating = input("Please enter a number 1-10. ")

#use regex to check date format
#date = input('What is today\'s date? Please follow the mm/dd/yyyy format. ')

#while re.match(r'(\d{2}(\/)\d{2}(\/)\d{4})', date):
    #or (^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4})
    #print('Error. Please follow directions. ')
    #rating = input("Please follow the mm/dd/yyyy format.  ")
#print('The date is: ' + date)


goodbye()


#while rating == re.match('[1-10]', rating):


        #while True:
            #if int(rating) >0 & <11:
                #break
              #print("Please enter a number between 1-10")