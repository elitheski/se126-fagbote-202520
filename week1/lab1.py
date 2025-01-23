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
#VARIABLE VOCABYULARY:
#difference - calculates the difference between the people attending and the mamimum ammount of people that can attend the meeting
#people     - stores the number of people attenind the meetiong to be used in the difference function
#max_cap    - stores the maximum ammount of people that can attend the meeting 
#response   - used to ask the user if they would like to add more information
#ans        - used to store the answer for if the user would like to continue
#ppl        - stores the number of people attendning the meeting 
#max        - stores the maximum number of people allowed to enter the meeting
#allow      - stores the answer of the function difference
#answer     - used to conintue the loop
#abs_x      - used to do the aboslue value so eveyr number returned to allow is positive

def difference(people,max_cap):
    
    diff = max_cap - people
    abs_x = abs(diff)

    return abs_x

def response():
    ans = input("Would you like to continue and enter another meetings attendance information? [y/n]").lower()

    while ans != "y" and ans !="n":
        print("***INVALID STATETEMENT***")
        ans = input("Would you like to continue and enter another meetings attendance information? [y/n]").lower()
    return ans 

print ("Welcome to the meetiong room program!")

answer = "y"
while answer == "y":
    ppl = float(input("How many people will be attending this meeting? "))
    max = float(input("Whats the maixmum capacity for the meeting? "))
    allow = difference(ppl,max)
  

    if ppl<= max:
        print(f"{allow} people can be added to the meeting and still meet the fire regulations")
    elif ppl>max:
        print(f"{allow} people must be removed from the meeting to meet fire regulations")



    answer = response()


print ("Goodbye, thank you for using my program")

