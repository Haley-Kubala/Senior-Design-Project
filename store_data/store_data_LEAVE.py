'''
This script will take the initial data when the student leaves
and store it in a text file so we can access it later when the
student returns.
'''
import argparse

def main(args):
    leave_info_file = open('leave_info_file', 'w')
    leave_info_file.write("ID : %s Time out : %s" % (args["ID"], args["START_TIME"]))

'''maybe create a function that creates a dat time and formats it as
    a string. put it in utils library and it can be called on the return script
'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ID", help="student ID needs to be entered")
    parser.add_argument("START_TIME", help="beginning time stamp")
    args = vars(parser.parse_args())
    main(args)
