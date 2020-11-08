import csv
from csv import DictWriter, DictReader

#create column headers for users.csv
#def list_history():
with open("users.csv", "r") as csv_file:
    columns = ['Username', 'Name', 'Date', 'Daily Journal', 'Activity Log', 'Daily Rating']
    csv_reader = csv.DictReader(csv_file, fieldnames=columns, delimiter=',')
    for lines in csv_reader:
            print(lines['Username'], lines['Name'], lines['Date'], lines['Daily Journal'], lines['Activity Log'], lines['Daily Rating'])









