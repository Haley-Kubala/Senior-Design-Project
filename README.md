Senior Design Project - 2017

Our goal for the project is to create a small device that allows teachers
to keep track of how long people use the hall pass, how often, as well as who
uses the pass. Other features could be added if we have time to do so.

Creators : Haley Kubala, Annie Williamson, David Roherbaugh

The Device utilizes an arduino, a raspberry pi, and a lcd touch screen.
We will be 3D printing the case that contains all of the parts.

Software Components : we will need to create a database, preferably a mongo
database to store all of the information for each student. There will need to
be code written to handle retrieving information from the touch screen,
storing that information in the database, updating the information. At the
moment this is all I can think of, but I'm sure there will need to be more
software written to tackle this.

The databse will need to store the students name, id, the length they've taken
the pass and the number of times they have taken the pass.
Ex. {"Name" : "",
     "ID" : "",
     "time" : "",
     "pass count" : ""}

Flow Chart(kind of):
(1) Create a the database on the raspberry pi that will store the
information(student name, id, etc.)
    -does this need to be formated or can wae add stuff to it from a script?
(2) have a script that reads a text file with the student information and then
appropriately formats it and stores it in the database
    -remember how to parse text files, set up connection to database,
    add information to databse using a script
    -needs error handling for when student list is updated
    (does student already exist? other possibilities??)
(3) when student enters identification the arduino will capture that i
nformation from the touch pad and send it to the pi
(4) pi will run a script that will
  A. check if information is valid
  B. make a connection to database
  C. reads through the database and finds a match for the ID
  D. it will incrememnt the password count and start a timer.
(5)somehow something will trigger the timer to stop and then store the total time the student was gone.
