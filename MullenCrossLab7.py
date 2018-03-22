# Programmers: Natalie Cross and Ethan Mullen
# Course:  CS151.01, Professor Franceschi
# Date: 3/20/18
# Lab Assignment:  7
# Problem Statement: Calculates the maximum profit and its movie title
# Data In: Input file from user
# Data Out: Movie title with maximum profit
# Other files needed:  algorithm.txt, movies.csv, test.csv
# Credits: N/A


#Create a function to find and test the user input for the file
def input_function():
    file = input("Please enter the input file: ")
    #First error check using a while loop; ensure that they input the correct file name
    while file != "movies.csv":
        file = input("Please enter the input file: ")
    #Make sure that the file opens using a try/except block
    try:
        movies_file = open("movies.csv", "r")
    except FileNotFoundError:
        print("Sorry, the file does not exist.")
    return file

#Create a function to calculate the maximum profit and movie title for a movie in the input file
def profit(filename):
    #Initialize the max_profit to 0 to keep track of the maximum profit in the file
    max_profit = 0
    movies_file = open(filename, "r")
    #Use a for loop to process each line
    for line in movies_file:
        release_date, movie_title, budget, gross = line.split(",")
        budget = float(budget)
        gross = float(gross)
        #If the profit for the movie in the current line is greater than the previous maximum profit, reassign the
        #  variable
        if (gross - budget) > max_profit:
            max_profit = gross - budget
            max_profit_movie = movie_title
    return str(max_profit_movie) + ": $" + str(max_profit)

#Create a function to write the title, release date, and profit for each movie
def writing(file_from, file_to):
    movies_file_new = open(file_to, "w")
    file = open(file_from, "r")
    #Use a for loop to process each line
    for line in file:
        release_date, movie_title, budget, gross = line.split(",")
        budget = float(budget)
        gross = float(gross)
        profit = gross - budget
        #Use the print function to write to the new file
        print(release_date, ",", movie_title, ",", "Profit = ", profit, sep = "", file = movies_file_new)

#Create a main function to call all other functions and output the results
def main():
    print("This program will calculate the maximum profit for a film within an input file.")
    input_function()
    print("The movie with the maximum profit is: ", profit("movies.csv"))
    writing("movies.csv", "moviesnew.csv")
main()




