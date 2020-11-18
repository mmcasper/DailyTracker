import re
import csv

def goodbye():
    print('Thank you for checking in today!')

#test username for whitespace
test = True
while test ==  True:
    username = input('Please create a username without any spaces. ')

    if re.search(r'\s', username):
        print('Please be sure there are no spaces in your username. ')
        test = True
    else:
        test = False

if username == (''):
    username = ('no input')


#use regex to validate rating
answer = True
while answer == True:
    rating = input('What is your rating for this day on a scale of 1-10? ')

    if not re.match(r'\b([1-9]|10)\b', rating):
        print('Error. Please follow directions. ')
        answer = True
    else:
        print('Your rating is: ' + rating)
        answer = False

#use regex to check date format
answer = True
while answer == True:
    date = input('Please enter the date in the mm/dd/yyyy format?. ')

    if not re.match(r'(\d{2}(\/)\d{2}(\/)\d{4})', date):
        print('Please follow the correct format for date: mm/dd/yyyy. ')
        answer = True
    else:
        print('The date is: ' + date)
        answer = False

goodbye()


#while rating == re.match('[1-10]', rating):


        #while True:
            #if int(rating) >0 & <11:
                #break
              #print("Please enter a number between 1-10")