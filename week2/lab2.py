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


print(f"{'Type':10}  {'Brand':10}  {'CPU':5}  {'RAM':5}  {'1st D':5}  {'# HDD':5}  {'2nd D':5}  {'OS':5} {'YR':5}")
 
with open("text_files/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        type = rec[0]
        brand = rec[1]
        cpu = rec[2]
        ram = rec[3]
        disk1 = rec[4]
        hdd = rec[5]
       # disk2 = rec[6]
       # os = rec[7]
        
        if rec[0] == "D":
            type = "Desktop"
        else:
            type = "Laptop"
       
        if rec[1] == "DL":
         brand = "Dell"
        elif rec[1] == "GW":
           brand = "Gateway"

        if rec[5] == "1":
            disk2 = ""
            os = rec[6]
            yr = rec[7]
        else:
           disk2 = rec[6]
           os = rec[7]
           yr = rec[8]

        print(f"{type:10}  {brand:10}  {cpu:5}  {ram:5}  {disk1:5}  {hdd:5}  {disk2:5}  {os:5} {yr:5}")
 
