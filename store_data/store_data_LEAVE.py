'''
This script will take the initial data when the student leaves
and store it in a text file so we can access it later when the
student returns.
'''
import argparse
import datetime
from datetime import date
import time

def main(args, datetime_string):
    leave_info_file = open('leave_info_file', 'w')
    leave_info_file.write("ID : %s , time out : %s "  % args["ID"], datetime_string)


def create_date():
    date_time = datetime.datetime.now().time
    date_time.strptime("%m%d%y")
    return date_time


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ID", help="student ID needs to be entered")
    #parser.add_argument("START_TIME", help="beginning time stamp")
    args = vars(parser.parse_args())
    datetime_string = create_date()
    main(args, datetime_string)
