#W3D2 - List Review - 1Dimensional Lists & Parallel Lists

#this file uses: class_grades.csv 

#--IMPORTS----------------------------------
import csv
#--FUNCTIONS--------------------------------

#--MAIN EXECUTING CODE----------------------

total_records = 0 
#W3D2 - List Review - 1Dimensional Lists & Parallel Lists

#this file uses: class_grades.csv 

#--IMPORTS----------------------------------
import csv
#--FUNCTIONS--------------------------------

#--MAIN EXECUTING CODE----------------------

total_records = 0 

#createan empty list for every potential field
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []

with open("text_files\class_grades.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        total_records += 1

        #fname = rec[0]

       # print (fname)
       #store data from current record to corresponding lists (each fielf is its own!)
       #.append() --> data dispersed across lists, connectedby the same index
        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

#we are disconected
#processing lists -- USE A FOR LOOP 
#for loops are used for data processing
for index in range (0, len(firstName)):
    #for every line, index will start at 0 and run up to (not including)  the length (# of items)
    print(f"INDEX {index}: {firstName[index]:10}  {lastName[index]:10}  {test1[index]:3}  {test2[index]:3}  {test3[index]:3}")


#create a new list to hold each studets avg test score
avg = []

for i in range (0, len(test1)):

    a = (test1[i] + test2[i] +test3[i]) / 3
    avg.append(a)

print(f"INDEX #: {'FIRST':10}  {'LAST':10}  {'T1':3}  {'T2':3}  {'T3':3} {'AVG'}")
print("-----------------------------------------------------------------------------")

for index in range (0, len(firstName)):
    #for every line, index will start at 0 and run up to (not including)  the length (# of items)
    print(f"INDEX {index}: {firstName[index]:10}  {lastName[index]:10}  {test1[index]:3}  {test2[index]:3}  {test3[index]:3} {avg[index]:.2f}")
print("-----------------------------------------------------------------------------")

#calc the entire class avg using a loop to add each student's avg to the class total
total_avg = 0
for i in range(0, len(avg)):
    total_avg += avg[i]

class_avg = total_avg / len(avg)
print (f"\nTOTAL RECORDS: {total_records}\nCURRENT CLASS AVERAGE: {class_avg:.2f}\n\nGoodbye!")
