#connect to mongo database
#connect to mongo collection
#create new document in collection
#retrieve ID and TIME STAMP from storage file

import argparse
import datetime
from datetime import date
import time

#def main(args):
end_date_time = datetime.datetime.now()
with open('leave_info_file') as leave_info_file:
    ID_leave_time_stamp = leave_info_file.read()
    print type(ID_leave_time_stamp)
