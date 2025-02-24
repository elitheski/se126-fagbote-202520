#Elijah Fabote
#W7D2 Lab 6
#2-18-2025 [72D2]
#Program Promt:
'''Store the file data into 1D parallel lists, then use the appropriate searching algorithms for the menu system options.
Your program should give your user the following menu:
Personal Library Menu
1. Show All Titles – list all book data to the user alphabetically by title
2. Search by Title – allow for an entire title or a title key word
3. Search by Author – show all titles of the searched-for author
4. Search by Genre - show all titles of the searched-for genre
5. Search by Library Number – only allow for one specific library number item
6. Show All Available – show all titles with status “available”
7. Show All On Loan - show all titles with status “on loan”
8. EXIT
When your user runs any of the options 1 – 7, show all data associated with the search [Library Number, Title, Author,
Genre, Page count, Status]. Do not allow the program to end unless the user chooses option 8 to exit. All searches
should not be case sensitive.
'''

#------------IMPORTS------------------
import csv

#-------------FUNCTIONS-------------------
def display(x, records):
    """PARAMETERS:
      x   signifier for if we are printing a single record or multiple
      when x != "x" it is an integere index and we have one value, otherwise we have multiple
        records the length of a list we are going to process through (# of loops/prints)"""
    print(f"{'Library Num':15}   {'Title':35}   {'Author':20}   {'Genre':15}   {'Page Count':10}    {'Status':10}")
    print("--------------------------------------------------------------------------------------------------------------------------")
    if x != "x":
        #printing one record
        print(f"{lib_num[x]:15}   {title[x]:35}   {author[x]:20}    {genre[x]:15}    {page_ct[x]:10}    {status[x]:10}")
        print("--------------------------------------------------------------------------------------------------------------------------")

    elif found:
        #priniting stuff based on the found 
        for i in range(0, records):
            print(f"{lib_num[found[i]]:15}   {title[found[i]]:35}   {author[found[i]]:20}    {genre[found[i]]:15}    {page_ct[found[i]]:10}    {status[found[i]]:10}")
            print("--------------------------------------------------------------------------------------------------------------------------")

    else:
        for i in range(0, records):
            print(f"{lib_num[i]:15}   {title[i]:35}   {author[i]:20}    {genre[i]:15}    {page_ct[i]:10}    {status[i]:10}")
            print("--------------------------------------------------------------------------------------------------------------------------")


def swap (i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp



#-------------------------MAIN CODE----------------------------------

#First we crate lists for each data type
lib_num = []
title = []
author = []
genre = []
page_ct = []
status = []

#connecting to the file
with open ("text_files/book_list.csv") as csvfile:
    file = csv.reader(csvfile)
    #Giving the empty lists data
    for rec in file:
        lib_num.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        genre.append(rec[3])
        page_ct.append(rec[4])
        status.append(rec[5])


print("Welcome to the Library Search Program!")


ans = input("Would you like to enter the search menu? [y/n]: ").lower()

#error trap
while ans != "y" and ans != "n": 
    print("***INVALID ENTRY***")
    ans = input("Would you like to enter the search menu? [y/n]: ").lower()

#main searching loop
while ans == "y":
    #menu
    print("\tPersonal Library Menu")
    print("1. Show by Title")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Search by Genre")
    print("5. Search by Library Number")
    print("6. Search by Availbe")
    print("7. Search by Loan")
    print("8.EXIT")
    

    choice = input("Enter what number of the menu selction you want to do: ")

    #validity check for user using "not in"
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("*****INALID ENTRY!****\nPlease try again")

    if choice == "8" :
        ans = "n"
        

    elif choice == "1":
         found = []
         #BUBBLE SORT from ascedning alpha character
         for i in range(0, len(lib_num) - 1):
            for j in range(0, len(lib_num) - 1):
                if lib_num[j] > lib_num[j + 1]:
                    swap(j, lib_num)
                    swap(j, title)
                    swap(j, author)
                    swap(j, genre)
                    swap(j, page_ct)
                    swap(j, status)

                    display("x", len(lib_num))


    elif choice == "2":
        print("\nYou choose search by TITLE")
        search = input("Enter the TITLE you're looking: ").lower()
        found=[]
        for i in range(0, len(lib_num)):
            if search == title[i].lower():
                found.append(i) #this adds the found data search to the list 

        if not found: #if search is not found
            print(f"Sorry your search for {search} was not found ;C")
            print()
        else:
            display("x", len(found))
    
    elif choice == "3":
        print("\nYou choose search by AUTHOR")

        search = input("Enter the AUTHOR you're looking: ").lower()
        found = []
        for i in range(0, len(lib_num)):
             if search == author[i].lower():
                found.append(i) #this adds the found data search to the list 

        if not found: #if search is not found
            print(f"Sorry your search for {search} was not found ;C")
            print()
        else:
            display("x", len(found))
        
    elif choice == "4":
       print("\nYou choose search by GENRE")
       search = input("Enter the GENRE you're looking: ").lower()
       found = []
       for i in range(0, len(lib_num)):
            if search == genre[i].lower():
                found.append(i) #this adds the found data search to the list 

       if not found: #if search is not found
            print(f"Sorry your search for {search} was not found ;C")
            print()
       else:
            display("x", len(found))
    
    elif choice == "5":
       print("\nYou choose search by LIBRARY NUMBER")
       search = input("Enter the NUMBER you're looking: ").lower()
       found = []
       for i in range(0, len(lib_num)):
            if search == lib_num[i].lower():
                found.append(i) #this adds the found data search to the list 

       if not found: #if search is not found
            print(f"Sorry your search for {search} was not found ;C")
            print()
       else:
            display("x", len(found))
    
    elif choice == "6":
       print("\nYou choose search by AVAILIBILITY")
       search = "available"
       found = []
       for i in range(0, len(lib_num)):
            if search == status[i].lower():
                found.append(i)
        
       display("x", len(found))

    elif choice == "7":
       print("\nYou choose search by ON LOAN")
       search = "on loan"
       found = []
       for i in range(0, len(lib_num)):
            if search == status[i].lower():
                found.append(i)
        
       display("x", len(found))
       
print("\n\nThank you for using my program, GOODBYE!\n\n\n")
