#Elijah Fagbote
#InClassLabWk2

#Program Prompt
"""The csv file classLab2.csv contains a list of rooms, the maximum number of people that the room
can accommodate, and the number of people currently registered for the event. Write a program that
displays all rooms that are over the maximum limit of people and the number of people that have to
be notified that they will have to be put on the wait list. After the file is completely processed the
program should display the number of records processed and the number of rooms that are over the
limit."""
#Variable Dictionary:
#difference - used to displlay the how many people are over the capcity of the rooms
# total_rec - used to store the data of how many total rooms there are 
# room_over - used to store how many rooms are over capacity
# file      - used to read the informations from the classLab2.csv file 
#name       - used to store the names in the csv file
#max        - used to store the max capacities in the csv file
#ppl        - used to store how many people are attenind the specific rooms
#remaining  - used to store the answer for difference 

#-----Imports--------------
import csv
#----Functions--------------
def difference(people, max_cap):
    
    diff = max_cap - people 
    
    return diff 

#---Main Executing Code------------------------

total_rec = 0
room_over = 0

#------connected to file-------------------------
print(f" {'NAME':20}    {'MAX':5}   {'PPL':5}    {'OVER'}")
print("-----------------------------------------------------------------")
with open("text_files/classLab2.csv") as csvfile:
    #indent one level while connected to the file
    file = csv.reader(csvfile)

    for rec in file:
        #below code occurs for record in the file 

        #assign each field data value to a name
        name = rec[0]
        max = int(rec[1])
        ppl = int(rec[2])

        #call the difference() to find people over/under capacity
        remaining = difference(ppl, max)

        #count and display the capacity that are over capacity (ramining is negative)
        if remaining < 0:
            room_over += 1
            print(f"{name:20}   {max:5}   {ppl:5}   {abs(remaining):5}")
        total_rec += 1

#-----disconnected from file----------------------------
#display final data
print(f"\nRooms currently over capacity: {room_over}")
print(f"Total rooms in file: {total_rec}")

