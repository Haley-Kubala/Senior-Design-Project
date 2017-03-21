'''
This script will take the initial data when the student leaves
and store it in a text file so we can access it later when the
student returns.
Questions? how will it write to a file if already exists?
'''
import argparse
import datetime
from datetime import date
import time

def main(args):
    date_time = datetime.datetime.now()
    with open('leave_info_file', 'w') as leave_file:
        leave_info_file.write(" %s , %s "  % (args["ID"], date_time))




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ID", help="student ID needs to be entered")
    #parser.add_argument("START_TIME", help="beginning time stamp")
    args = vars(parser.parse_args())
    main(args)
