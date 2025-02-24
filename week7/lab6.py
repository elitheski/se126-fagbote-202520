#Elijah Fabote
#W7D2 Lab 6
#2-20-2025 [72D2]
#Program Promt:
"""6. (Absolute C++, 3rd Edition. Savitch, Walter. P. 223 #10)
Write a Python program using lists (1D or 2D) to assign passengers seats in an airplane. Assume a
small airplane with seat numbering as follows.
Row
1 A B C D
2 A B C D
3 A B C D
4 A B C D
5 A B C D
6 A B C D
7 A B C D
The program should display the seat pattern, with an ‘X’ making the seats already assigned. For
example, after seats 1A, 2B and 4C are taken the display should look like this:
Row
1 X B C D
2 A X C D
3 A B C D
4 A B X D
5 A B C D
6 A B C D
7 A B C D
After displaying the seats available, the program prompts for the seat desired, the user types in a seat
and then the display of available seats is updated. This continues until all seats are filled or until the
user signals that the program should end. If a user types in a seat that is already assigned, the
program should say that the seat is occupied and ask for another choice.
• You must use a function to display the seating map
• You must use a function that asks the user in they want to continue reserving seats or stop.
The function should only accept an uppercase or lowercase ‘y’ or ‘n’."""

#---FUNCTIONS-----------
def map():
    
    for i in range(len(seatsA)):
        print(f"{i+1}  {seatsA[i]}\t{seatsB[i]}\t\t{seatsC[i]}\t{seatsD[i]}")

def choice():
    #promtps the user is they want to continue selecting seats
    ans = input("Would you like to continue seletcing seats? [y/n]").lower()
    while ans !="y" and ans != "n":
        print("***INVALID ENTRY***")
        ans = input("Would you like to continue seletcing seats? [y/n]: ").lower()

    return ans


seatsA = ['A','A','A','A','A','A','A']
seatsB = ['B','B','B','B','B','B','B']
seatsC = ['C','C','C','C','C','C','C']
seatsD = ['D','D','D','D','D','D','D']


print ("Weclome to the air plan seating program!\n")

ans = input("Would you like to choose your seat? [y/n]").lower()
while ans !="n" and ans!="y":
    print("***INVALID ENTRY****")
    ans = input("Would you like to choose your seat? [y/n]").lower()

while ans == "y":
    #displays the seats for user
    print("These are the seats availible\n")
    print("Row")
    map()
    #input from user
    row = int(input("What row could you like to select [1-7]: "))
    seat = input("What seat do you want to choose [A/B/C/D]:  ")

    #manipluating the data

    if seat.upper() == "A":
        #this makes it so if the seats are not taken it appends (or adds)/updates the list

        if seatsA[row - 1] != "X":
            seatsA[row -1] = "X"
            print("Here is the updated seat chart:\n")
            print("Row")
            for i in range(len(seatsA)):
                print(f"{i + 1} {seatsA[i]}\t{seatsB[i]}\t\t{seatsC[i]}\t{seatsD[i]}")
            ans = choice()   
        else:
            print(f"Sorry, seat {row}{seat} is taken")
            ans = choice() 
            
    
    elif seat.upper() == "B":
        if seatsB[row-1] != "X":
            seatsB[row -1] = "X"
            print("Here is the updated seat chart:\n")
            print("Row")
            for i in range(len(seatsA)):
                print(f"{i + 1} {seatsA[i]}\t{seatsB[i]}\t\t{seatsC[i]}\t{seatsD[i]}")
            ans = choice()     
        else:
            print(f"Sorry, seat {row}{seat} is taken")
            ans = choice() 

    elif seat.upper() == "C":
        if seatsC[row-1] != "X":
            seatsC[row -1] = "X"
            print("Here is the updated seat chart:\n")
            print("Row")
            for i in range(len(seatsA)):
                print(f"{i + 1} {seatsA[i]}\t{seatsB[i]}\t\t{seatsC[i]}\t{seatsD[i]}")
            ans = choice()     
        else:
            print(f"Sorry, seat {row}{seat} is taken")
            ans = choice() 

    elif seat.upper() == "D":
        if seatsD[row - 1] != "X":
            seatsD[row -1] = "X"
            print("Here is the updated seat chart:\n")
            print("Row")
            for i in range(len(seatsA)):
                print(f"{i + 1} {seatsA[i]}\t{seatsB[i]}\t\t{seatsC[i]}\t{seatsD[i]}")
            ans = choice()            
        else:
            print(f"Sorry, seat {row}{seat} is taken")
            ans = choice() 



print("Thank you for using my program :D")   
