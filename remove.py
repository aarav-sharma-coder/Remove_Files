import os
import sys
import datetime

path_entered = input("Enter your desired path: ")
# age = input("Enter your desired deadline")
age = 30
confirmation_message = ''


if not os.path.exists(path_entered):
    print("Please provide a valid path")
    sys.exit(1)

if os.path.isfile(path_entered):
    print("Please provide a directory path")
    sys.exit(2)

today_date = datetime.datetime.now()

for each_file in os.listdir(path_entered):
    each_file_path = os.path.join(path_entered, each_file)
    if os.path.isfile(each_file_path):
        file_creation_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        difference_in_days = (today_date - file_creation_date)
        if str(difference_in_days) > str(age):
            print(each_file_path, difference_in_days)
            confirmation_message = input("Do you want to delete the above files? ")
            if str(confirmation_message) == "yes":
                os.remove(each_file_path)
                print("They got deleted")