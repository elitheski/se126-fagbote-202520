#Elijah Fabote
#W2D2 Lab 2
#1-16-2025 [W2D2]

#PROGRAM PROMT: 
'''You have been asked to produce a report that lists all the computers in the csv file
filehandling.csv.
Your report should look like the following sample output.
The last line should print the number of computers in the file.
Organization of the csv file:'''


#Import
import csv

print(f"{'Type':10}  {'Brand':10}  {'CPU':5}  {'RAM':5}  {'1st Disk':5}  {'No HDD':5}  {'2nd Disk':5}  {'OS'} {'YR'}")
 
with open("text_files/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        type = rec[0]
        brand = rec[1]
        cpu = rec[2]
        ram = rec[3]
        disk1 = rec[4]
        hdd = rec[5]
        disk2 =rec[6]
        os = rec[7]
        yr = rec [8]
        
       print(f"{type:10}  {brand:10}  {cpu:5}  {ram:5}  {disk1:5}  {'No HDD':5}  {'2nd Disk':5}  {'OS'} {'YR'}")
 
