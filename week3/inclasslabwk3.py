#Elijah Fabote
#In Class Lab 
#1-16-2025 [W3D2]

#PROGRAM PROMT:Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.

#Elijah Fabote
#W2D2 Lab 2
#1-16-2025 [W2D2]

#PROGRAM PROMT: 
'''You have been asked to produce a report that lists all the computers in the csv file
filehandling.csv.
Your report should look like the following sample output.
The last line should print the number of computers in the file.
Organization of the csv file:'''

#IMPORT
import csv

#MAIN CODE

#created list for every possible field
type_list= []
brand_list = []
cpu_list = []
ram_list = []
disk1_list = []
hdd_list = []
disk2_list = []
os_list = []

#Connected to the file
with open("text_files/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)
    #assigning names to files
    for rec in file:
        type = rec[0]
        brand = rec[1]
        cpu = rec[2]
        ram = rec[3]
        disk1 = rec[4]
        hdd = rec[5]
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
    #using the names of the files to connect them to the newly made lists so that it knows which column to add data from

for rec in file:
    type_list.append(type)
    brand_list.append(brand)
    cpu_list.append(cpu)
    ram_list.append(ram)
    disk1_list.append(disk1)
    hdd_list.append(hdd)
    disk2_list.append(disk2)
     

print(f"{'Type':10}  {'Brand':10}  {'CPU':5}  {'RAM':5}  {'1st D':5}  {'# HDD':5}  {'2nd D':5}  {'OS':5} {'YR':5}")
 
for i in range (0, len(type)):
    

    print(f"{type[i]:10}  {brand[i]:10}  {cpu[i]:5}  {ram[i]:5}  {disk1[i]:5}  {hdd[i]:5}  {disk2[i]:5}  {os[i]:5}")
