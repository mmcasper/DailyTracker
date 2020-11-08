from csv import DictReader, DictWriter

#function to add new rows to csv dictionary
def append_dict_as_row(file_name, dict_of_elem, field_names):
    #open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
    #Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
    #Add dict as wor in the csv
        dict_writer.writerow(dict_of_elem)

#collect fields from user
username = input('Please create a username without any spaces: ')
#test for whitespace
name = input('What is your first name? ')
date = input('What is today\'s date? Please follow the mm/dd/yyyy format. ')
#test for correct formatting of date
journal = input('Would you like to record any thoughts for this day? ')
activity = input('Would you like to record any physical activity for the day? ')
rating = input('What is your rating for this day on a scale of 1-10? ')

field_names = ['Username', 'Name', 'Date', 'Daily Journal', 'Activity Log', 'Daily Rating']
row_dict = {'Username' : '{}'.format(username), 'Name' : ' {}'.format(name), 'Date' : ' {}'.format(date), 'Daily Journal' : ' {}'.format(journal),'Activity Log' : ' {}'.format(activity),'Daily Rating' : ' {}'.format(rating)}
append_dict_as_row('users.csv', row_dict, field_names)

