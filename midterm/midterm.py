#Elijah Fagbote
#Midterm Pratical
#Prompt choice 3:
"""Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have
been fully populated with file data, create a new list to hold a student ID value for each student. The first
student in the file should have an ID of 10001, each student’s ID should be unique, and the ID values
should not exceed 10021. Once the new list is populated, process through the five lists to display all of
the student data to the user as well as the total number of records in the file.
Once all of the data has been displayed, write all of the list data to a new file called
‘midterm_choice3.csv’, where each student’s information is found on one record in the file and their
data is separated by a comma (additional empty line in resulting file is okay).
Finally, create a sequential search program that allows a user to repeatedly search the student database
information stored in the lists based on the following menu:
Student Search
1. Search by LAST NAME
2. Search by DEPARTMENT
3. EXIT"""

#Imports
import csv
import random

 
#assigning names for the fields 

first_name = []
last_name = []
department = []
gpa = []
id = []
#connecting to the file
with open ("text_files\students.csv") as csvfile:
    file = csv.reader(csvfile)

    #assigning the data to the assigned names
    for rec in file:
        first_name.append(rec[0])
        last_name.append(rec[1])
        department.append(rec[2])
        gpa.append(rec[3])

#Neatly making columns
print(f"{'First':10}     {'Last':10}    {'Department':10}    {'gpa':10}    {'Id':10}")
print("-------------------------------------------------------------------")
for i in range(0, len(first_name)):
    print (f"{first_name[i]:10}     {last_name[i]:10}    {department[i]:10}    {gpa[i]:10}    {id:}")    
print("-----------------------------------------------------------------------------")    
print(f"TOTAL STUDENTS IN FILE: {len(first_name)}")

found = -1
option = input("Student Search\n1.Search by LAST NAME\n2.Search by DEPARTMENT\n3.EXIT\n")

if option == 1:
    ans=input("Enter the last name you wish to search for: ")
    for i in range(0, len(last_name)):
      if ans.lower() == last_name[i].lower():
       found = i

    if found != -1:
        print(f"Your search for {ans} was FOUND! Here is their data")
        print(f"{first_name[found]}   {last_name[found]}   {department[found]}   {gpa[found]}")
    else:
       print(f"Your search for {ans} was not FOUND! Here is their data")
elif option == 2:
    ans= input("Enter the department you wish to  search for")
    for i in range(0, len(last_name)):
        if ans.lower() == last_name[i].lower():
         found = i

    if found != -1:
       print(f"Your search for {ans} was FOUND! Here is their data")
       print(f"{first_name[found]}   {last_name[found]}   {department[found]}   {gpa[found]}")
    else:
       print(f"Your search for {ans} was not FOUND! Here is their data")
else:
   print("Goodbye")