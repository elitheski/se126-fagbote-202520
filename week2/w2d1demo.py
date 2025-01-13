#W2D1 - Text File Handling - Introduction

#STEP 1: import the csv (comma separated value) library
import csv

total_records = 0 #the total number of records (rows) in the file

#STEP 2:
#connecting to the file's path - switch \ to /
#-----connected to file--------------------------------------------
print(f"\n{'NAME':10} \t {'NUM':3} \t {'COLOR'}") #HEADER PRINT
print("------------------------------------")
with open("text_files/simple.csv") as csvfile:

    #allow processor to read the file data
    file = csv.reader(csvfile)

    #STEP3: process through every (row) in the file
   
    for record in file:
        #add +1 to total_records
        total_records += 1

        #print(record) #the list view of each record (row)

        name = record[0]     #name field
        number = record[1]   #number field
        color = record[2]    #color field

        print(f"{name:10} \t {number:3} \t {color.title()}")
#-----disconnected from file--------------------------------------
print("------------------------------------")
print(f"\nTOTAL RECORDS: {total_records}\n")