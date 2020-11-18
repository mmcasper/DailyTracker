import csv
from csv import DictReader, DictWriter
import list_entries
import re

#function to add new rows to csv dictionary
def append_dict_as_row(file_name, dict_of_elem, field_names):
    #open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
    #Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
    #Add dict as row in the csv
        dict_writer.writerow(dict_of_elem)

#function to say sign off
def goodbye():
    print('Thank you for checking in today {}!'.format(name))

#create welcome 
print("Welcome to your daily mood tracker. You will be asked for a daily rating after recording events and activities that may have affected that rating.")

#collect fields from user
username = input('Please create a username without any spaces: ')
#test for username for whitespace
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

#Collect and force input for first name
name_answer = True
while name_answer == True:
    name = input('What is your first name? ')
    if name == (''):
        print('Please enter your first name. ')
        name_answer = True
    else:
        name_answer = False

#Use regex to test for correct formatting of date
date_answer = True
while date_answer == True:
    date = input('Please enter the date in the mm/dd/yyyy format?. ')
    if not re.match(r'(\d{2}(\/)\d{2}(\/)\d{4})', date):
        print('Please follow the correct format for date: mm/dd/yyyy. ')
        date_answer = True
    else:
        print('The date is: ' + date)
        date_answer = False

journal = input('Please enter any thoughts you would like to record any thoughts for this day? ')
#create empty string output
if journal == (''):
    journal = ('no input')

activity = input('Please record any physical activity for the day? ')
#create empty string output
if activity == (''):
    activity = ('no input')

#Use regex to test for requested rating input
answer = True
while answer == True:
    rating = input('What is your rating for this day on a scale of 1-10? ')
    if not re.match(r'\b([1-9]|10)\b', rating):
        print('Error. Please follow directions. ')
        answer = True
    else:
        print('Your rating is: ' + rating)
        answer = False

#Create field names and assign input to that field
field_names = ['Username', 'Name', 'Date', 'Daily Journal', 'Activity Log', 'Daily Rating']
row_dict = {'Username' : '{},'.format(username), 'Name' : ' {},'.format(name), 'Date' : ' {},'.format(date), 'Daily Journal' : ' {},'.format(journal),'Activity Log' : ' {},'.format(activity),'Daily Rating' : ' {}'.format(rating)}

#Using function to write to csv file.
append_dict_as_row('users.csv', row_dict, field_names)

def get_input():
    response = input('Would you like to see your previous entries? y/n ')
    return response

if get_input() == 'y':
    list_entries.list_history()
    
else:
    pass

goodbye()






