#Elijah Fagbote
#In Class Lab
#1-27-2025 [W4D1]

#PROGRAM PROMT: 
# Part 1: Write a program that reads the data file (below) and stores the data into 1D parallel lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file.
# Part 2: Next, reprocess the lists to find each student's current average score, letter grade equivalent, and the class average.  While processing in the for loop, store each student's average into a new list called 'num_avg' and their letter grade into a list called 'let_avg'. Then, print each student's full information, record by record including average score and average letter equivalent.  After this print of the original file data from the lists, print to the console the total number of student's in the class along with the class numeric average.  
# Part 3: After your final display using the 1D parallel lists, create a sequential search program which allows the user to repeatedly utilize the following menu of search types. When a searched for item is found, display all student data to the console. When a search is compete and no matching data is found, alert the user. Search options 1 and 2 should only show one found student, where search option 3 should show a potential of multiple students.

#--IMPORTS---------------------
import csv

#--FUNCTIONS----------------------
def letter (num):
    if num >= 90:
        let = "A"
    elif num >=80:
        let = "B"
    elif num >=70:
        let = "C"
    elif num >=60:
        let = "D"
    elif num <60:
        let = "F"
    else:
        let = "ERROR"
    return let #the 'let' value will literlly replace the letter function call

