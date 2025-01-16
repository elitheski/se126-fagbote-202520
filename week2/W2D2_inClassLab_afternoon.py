#Elijah Fagbote
#InClassLabWk2

#Program Prompt:

#Variable Dictionary:

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
print(f" {'NAME':20}   {'MAX':5} {'PPL':5}   {'OVER':5}")
print("-----------------------------------------------------------------")
with open("text_files/classLab2.csv") as csvfile:
    #we mst indent one level while connected to the file
    file = csv.reader(csvfile)

    for rec in file:
        #below code occurs for record in the file 

        #assign each field data value to a friendl var name
        name = rec[0]
        max = int(rec[1])
        ppl = int(rec[2])

        #call the difference() to find people over/under capacity
        remaining = difference(ppl, max)

        #count and display the capacity that are over capacity (ramining is negative)
        if remaining < 0:
            room_over += 1
            print(f"{name:5}   {max:5}   {remaining:5}")

#-----disconnected from file----------------------------
#display final data
print(f"\nRooms currently over capacity: {room_over}")
print(f"Total rooms in file: {total_rec}")

