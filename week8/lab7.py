#Elijah Fabote
#W7D2 Lab 6
#2-27-2025 [72D2]
#Program Promt:
"""ccess the words.csv file and store the data to a dictionary, where each word in the file is a key of the dictionary and
the value stored to each key is the word’s corresponding definition. Then, create a repeatable program that allows a
user to interact with the dictionary based on the following menu:
My Programming Dictionary Menu
1. Show all words – Show all words and their definitions stored to the dictionary
2. Search for a word – Allow the user to enter a word and if it is in the dictionary, show its definition (tell the user if
the word is not in the dictionary)
3. Add a word – Allow a user to add a word and its definition to the dictionary if it does not already exist
4. EXIT
The program should not be case sensitive for user input, and the user should only be able to quit when they have
selected menu option number 4"""


#------Imports-------------------------------
import csv

#-------Functions-------------------------
#the menu
def menu():
    print("Dictionary Menu\n1.  Show all words\n2.  Search for a word\n3.  Add a word\n3.5 Show all the words in Alphabetical Order\n4.  EXIT")
    choice = input("Select what menu choice you want to use [1-4]: ")
    while choice not in ["1","2","3","3.5","4"]:
        print("***INVALID ENTRY***")
        choice = input("Select what menu choice you want to use [1-4]: \n")

    return choice

def swap (i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp


#----Main Executing Code-----------------------------------


#making the library
library = {}

#connecting to file 
with open("text_files\words.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        library.update({rec[0]: rec[1]})  

    print("Welcome to the programming dictionary!!!\n")
    
    
    ans ="y"
    while ans =="y":
        
        options = menu()
        if options == "4":
            print("Goodbye thank you for using my program :D")
            ans = "n"

        #prints all the words and deinitions
        elif options == "1":
            print("Here is all the words and their Definitions:\n")
            print(f"{'Word':5} : {'Definition'}")
            print("-" * 200)

            for word in library :
                print(f"{word.upper()} : {library[word]}")
            print("-" * 200)
          
          #utaizing sequential search for option 2
        elif options == "2":
            found = 0

            search = input("What WORD are you looking for: ")
            
            for word in library:
                if search.lower() == word.lower():
                    found = word
            if found != 0:
                print(f"We found your search for {search}, here is the context:  ")
                print("-" * 100)
                print(f"{found.upper():5} : {library[found]}")
                print("-" * 100)
            else:
                print(f"We could not find your search for {search}")
        
        #appending or adding a new word and definition to the end of the list
        elif options == "3":
            word = input("What WORD are you trying to add: ")
            definition = input("What's the deinition: ")
            
            library.update({word:definition})

'''        #Bubble Sort I think 
        elif options == "3.5":
         #BUBBLE SORT from ascedning alpha character
           for i in range(0, len(word) - 1):
            for j in range(0, len(word) - 1):
                if word[j] > word[j + 1]:
                    swap(j, word)
                    swap(j, definition)'''
        