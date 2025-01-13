#Elijah Fabote
#W1D2 Lab 1
#1-9-2025 [W1D2]

#PROGRAM PROMT
'''you will be writing one Python file for this project - it is a program that determines whether a
meeting room is in violation of fire regulations regarding the maximum room capacity. The
program will accept the maximum room capacity and the number of people attending the
meeting. If the number of people is less than or equal to the maximum room capacity, the
program announces that it is legal to hold the meeting and tells how many additional people may
legally attend. If the number of people exceeds the maximum room capacity, the program
announces that the meeting cannot be held as planned due to the fire regulation and tells how
many people must be excluded in order to meet the fire regulations. The user should be allowed
to enter and check as many rooms as they would like without exiting the program.'''

def difference(people,max_cap):
    
    diff = max_cap - people

    return diff

def response(response):
    response = input("would like to continue and enter another meeting’s attendance information? ").lower()
    while response !="y" or response!="n":
        print ("***INVALID ENTRY")
        response = input("Would like to continue and enter another meeting’s attendance information? ").lower()

print ("Welcome to the meeting room attendance program!")
room_n = input("What is the room name: ")
ppl = float(input("How many people are attending this meeting: "))
max = float(input("What are the maximum amount of people that can attend the meeting: "))

allow = difference(ppl,max)
print(allow)