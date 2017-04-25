import argparse
import regex

def is_Match(ID):
#connect to Mongo
#search for a matching ID from mongo database
#report results

def is_id_trash(ID):
   '''calls the appropriate script based on whether or not the ID passed from David is actually .
   :param ___: takes a
   :return: calls appropriate scrip based on the true/false options
   '''
   # use regex
    if len(ID) == 5 and ID.isdigit():
        return false
        #the string is not trash
    else: 
        return true
        #the string is trash
        # will prompt the user to re enter ID
    
        #If it does return false, I think this is where it would call one of David's functions
        #prompting the user to re-enter their ID

    



def main(args):
    enteredID = args['ID']
    #rework
    if is_id_trash(returningID)
        #call David with error message
        pass

    if is_Match(enteredID)
        pass
        #do reporting

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ID", help="student ID must match the one in the file")
    #change these arguments
    args = vars(parser.parse_args())
    main(args)
