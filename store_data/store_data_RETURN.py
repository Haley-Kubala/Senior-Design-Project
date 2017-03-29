#connect to mongo database
#connect to mongo collection
#create new document in collection
#retrieve ID and TIME STAMP from storage file

import argparse
import datetime
from datetime import date
import time


end_date_time = datetime.datetime.now()
with open('leave_info_file') as leave_info_file:
    ID_leave_time_stamp = leave_info_file.read()
    print type(ID_leave_time_stamp)
    info_list = ID_leave_time_stamp.split(" ")
    print info_list
    ID = info_list[1]
    date = info_list[2]
    time = info_list[3]
    print ID
    print date
    print time
