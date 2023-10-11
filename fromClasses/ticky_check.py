#!/usr/bin/env python3

#Created for final test in
#Using Python to Interact with the Operating System

import re
import operator
import csv

errors = {}
users = {}
file_path = "/home/student-02-fbd8fe4eb8ae/syslog.log"

with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        match_error = re.search("ERROR (\D*?)\(", line)
        match_user = re.search("\((\D*)\)",line)
        match_info = re.search("INFO", line)
        if match_error:
            error = match_error.group(1).strip()
            if error in errors:
                errors[error] += 1
            else:
                errors[error] = 1

        if match_user:
            user = match_user.group(1)
            if user not in users:
                users[user] = {"INFO": 0, "ERROR": 0}
            if match_info:
                users[user]["INFO"] += 1
            if match_error:
                users[user]["ERROR"] += 1

sorted_errors = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)
sorted_users = sorted(users.items())

error_header = ["Error", "Count"]
user_header = ["Username", "INFO", "ERROR"]

with open('error_message.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(error_header)
    writer.writerows(sorted_errors)

users_as_dict_list = [{"Username": key, "INFO": value["INFO"], "ERROR": value["ERROR"]} for key, value in sorted_users]

with open('user_statistics.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=user_header)
    writer.writeheader()
    for row in users_as_dict_list:
        writer.writerow(row)
