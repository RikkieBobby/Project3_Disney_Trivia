import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open("disney_trivia")
    leaderboard = SHEET.worksheet('leaderboard')


def get_user_name():
    """
    gets the name from the user for the trivia game,
    this function will run a while loop asking the user to input a name to the terminal
    the name must be at least 3 characters long and must not conatin numbers or syntax which
    is not letters, if the user inputs anything that isn't a letter, the loop will return an error and request
    the data again until the correct data is entered
    """
    while True:
        print("Welcome to the Disney Trivia game!")
        print("In this game you, the user, will answer a series of Disney based Trivia questions with a choice of answers")
        print("The game will calculate your score as you play and display the final score at the end, let's see if you can make it to the top 5!")
        print("First, let's start by entering your name\n")

        name = input("Enter your name here: ")
        if name.isalpha() and len(name) >= 3:
            return name
        else:
            print("Sorry, you must enter a name 3 letters long and only use letters, try again\n")
            continue
        


user_name = get_user_name()
print(f"Great! Your name for the game will be {user_name}.")
