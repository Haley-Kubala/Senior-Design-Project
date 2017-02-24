'''
This script will take the initial data when the student leaves
and store it in a text file so we can access it later when the
student returns.
'''
import argparse

leave_info_file = ('leave_info_file', 'w')

f.write('ID: 123')


parser = argparse.ArgumentParser()
parser.add_argument("ID", help="student ID needs to be entered")
parser.add_argument("START_TIME", help="beginning time stamp")
parser.add_argument("END_TIME", help="ending time stamp")
args = vars(parser.parse_args())
